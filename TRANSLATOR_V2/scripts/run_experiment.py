#!/usr/bin/env python3
"""
Translation Quality Experiment Runner

This script runs the full translation experiment:
1. Takes test sentences with 15+ words
2. Injects spelling errors at various rates (0% - 50%)
3. Runs each variant through the translation pipeline (EN → FR → HE → EN)
4. Measures vector distance between original and final translation
5. Generates a graph of spelling error % vs vector distance

Requirements:
    pip install sentence-transformers matplotlib anthropic

Usage:
    python run_experiment.py                    # Run full experiment
    python run_experiment.py --mock             # Run with mock translations (no API)
    python run_experiment.py --sentences-only   # Just show test sentences
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from spelling_error_injector import SpellingErrorInjector, ErrorStats
from embedding_similarity_local import LocalEmbeddingSimilarityChecker


@dataclass
class TranslationResult:
    """Result from a single translation pipeline run."""
    original_sentence: str
    input_with_errors: str
    error_rate: float
    actual_error_rate: float
    french_translation: str
    hebrew_translation: str
    final_english: str
    similarity_score: float
    vector_distance: float  # 1 - similarity


@dataclass
class ExperimentResult:
    """Complete experiment results."""
    timestamp: str
    test_sentences: List[str]
    sentence_lengths: List[int]
    error_rates: List[float]
    results: List[TranslationResult]
    summary: Dict


# ============================================================================
# TEST SENTENCES (15+ words each, as required by assignment)
# ============================================================================

TEST_SENTENCES = [
    # Sentence 1: 20 words - General/descriptive
    "The magnificent golden sunset painted the entire western sky with beautiful shades of orange, pink, and deep purple colors.",

    # Sentence 2: 18 words - Action/narrative
    "Every morning the dedicated young student walks through the peaceful park to reach her university campus on time.",
]

# Verify sentence lengths
for i, s in enumerate(TEST_SENTENCES):
    word_count = len(s.split())
    assert word_count >= 15, f"Sentence {i+1} has only {word_count} words (need 15+)"


# ============================================================================
# TRANSLATION FUNCTIONS
# ============================================================================

def translate_with_claude(text: str, source_lang: str, target_lang: str,
                         api_key: Optional[str] = None) -> str:
    """
    Translate text using Claude API.

    Args:
        text: Text to translate
        source_lang: Source language (e.g., "English", "French", "Hebrew")
        target_lang: Target language
        api_key: Anthropic API key (uses env var if not provided)

    Returns:
        Translated text
    """
    try:
        import anthropic
    except ImportError:
        raise ImportError("Please install anthropic: pip install anthropic")

    api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set. Use --mock for testing without API.")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Translate the following text from {source_lang} to {target_lang}.
Return ONLY the translation with no explanations or additional text.

Text to translate:
{text}"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()


def mock_translate(text: str, source_lang: str, target_lang: str) -> str:
    """
    Mock translation for testing without API.

    This simulates translation by making minor modifications to demonstrate
    the pipeline flow. In production, use translate_with_claude().
    """
    # Simple mock that preserves most meaning
    # In reality, this would be actual translation

    if source_lang == "English" and target_lang == "French":
        # Simulate EN -> FR
        replacements = {
            "The": "Le", "the": "le", "a": "un", "is": "est",
            "beautiful": "magnifique", "sunset": "coucher de soleil",
            "morning": "matin", "student": "étudiant", "walks": "marche",
            "park": "parc", "university": "université", "campus": "campus",
            "golden": "doré", "sky": "ciel", "colors": "couleurs",
            "orange": "orange", "pink": "rose", "purple": "violet",
            "deep": "profond", "young": "jeune", "peaceful": "paisible",
            "dedicated": "dévoué", "entire": "entier", "western": "occidental",
            "painted": "peint", "shades": "nuances", "magnificent": "magnifique",
            "through": "à travers", "reach": "atteindre", "her": "sa",
            "Every": "Chaque", "time": "temps", "on": "à"
        }
        result = text
        for eng, fr in replacements.items():
            result = result.replace(eng, fr)
        return result

    elif source_lang == "French" and target_lang == "Hebrew":
        # Simulate FR -> HE (just return mock Hebrew-like result)
        return "השקיעה המרהיבה צבעה את השמיים המערביים בגוונים יפים של כתום וורוד וסגול עמוק"

    elif source_lang == "Hebrew" and target_lang == "English":
        # Simulate HE -> EN (return slightly modified English)
        # This simulates the "drift" that occurs through translation
        if "sunset" in text.lower() or "שקיעה" in text:
            return "The magnificent golden sunset painted the western sky with beautiful shades of orange, pink, and deep purple."
        else:
            return "Every morning the dedicated young student walks through the peaceful park to reach her university campus on time."

    return text


def run_translation_pipeline(text: str, use_mock: bool = False,
                            api_key: Optional[str] = None) -> Tuple[str, str, str]:
    """
    Run the full translation pipeline: EN → FR → HE → EN

    Args:
        text: English text to translate
        use_mock: If True, use mock translations instead of API
        api_key: Optional API key for Claude

    Returns:
        Tuple of (french_text, hebrew_text, final_english_text)
    """
    translate = mock_translate if use_mock else lambda t, s, d: translate_with_claude(t, s, d, api_key)

    # Step 1: English → French
    french = translate(text, "English", "French")

    # Step 2: French → Hebrew
    hebrew = translate(french, "French", "Hebrew")

    # Step 3: Hebrew → English
    final_english = translate(hebrew, "Hebrew", "English")

    return french, hebrew, final_english


# ============================================================================
# EXPERIMENT RUNNER
# ============================================================================

def run_experiment(sentences: List[str] = None,
                  error_rates: List[float] = None,
                  use_mock: bool = False,
                  api_key: Optional[str] = None,
                  verbose: bool = True) -> ExperimentResult:
    """
    Run the full spelling error vs vector distance experiment.

    Args:
        sentences: Test sentences (uses TEST_SENTENCES if None)
        error_rates: Error rates to test (default: 0%, 10%, 20%, 25%, 30%, 40%, 50%)
        use_mock: If True, use mock translations
        api_key: Optional API key
        verbose: Print progress

    Returns:
        ExperimentResult with all data
    """
    if sentences is None:
        sentences = TEST_SENTENCES

    if error_rates is None:
        error_rates = [0.0, 0.10, 0.20, 0.25, 0.30, 0.40, 0.50]

    # Initialize components
    injector = SpellingErrorInjector(seed=42)
    similarity_checker = LocalEmbeddingSimilarityChecker()

    results: List[TranslationResult] = []

    if verbose:
        print("\n" + "=" * 70)
        print("TRANSLATION QUALITY EXPERIMENT")
        print("Pipeline: English → French → Hebrew → English")
        print("=" * 70)
        print(f"\nTest sentences: {len(sentences)}")
        print(f"Error rates to test: {[f'{r*100:.0f}%' for r in error_rates]}")
        print(f"Mode: {'Mock (no API)' if use_mock else 'Claude API'}")
        print()

    # Run experiments
    for sent_idx, sentence in enumerate(sentences):
        if verbose:
            print(f"\n--- Sentence {sent_idx + 1} ({len(sentence.split())} words) ---")
            print(f"Original: {sentence[:80]}...")

        for error_rate in error_rates:
            # Inject errors
            error_stats = injector.inject_errors(sentence, error_rate)

            if verbose:
                print(f"\n  Error rate: {error_rate*100:.0f}% (actual: {error_stats.actual_error_rate*100:.1f}%)")

            # Run translation pipeline
            try:
                french, hebrew, final_english = run_translation_pipeline(
                    error_stats.modified_text,
                    use_mock=use_mock,
                    api_key=api_key
                )
            except Exception as e:
                if verbose:
                    print(f"    ERROR: {e}")
                continue

            # Calculate similarity (compare ORIGINAL clean sentence to final translation)
            sim_results = similarity_checker.analyze(sentence, final_english)
            similarity = sim_results['similarity_score']
            distance = 1 - similarity

            result = TranslationResult(
                original_sentence=sentence,
                input_with_errors=error_stats.modified_text,
                error_rate=error_rate,
                actual_error_rate=error_stats.actual_error_rate,
                french_translation=french,
                hebrew_translation=hebrew,
                final_english=final_english,
                similarity_score=similarity,
                vector_distance=distance
            )
            results.append(result)

            if verbose:
                print(f"    Input:  {error_stats.modified_text[:60]}...")
                print(f"    Output: {final_english[:60]}...")
                print(f"    Similarity: {similarity:.4f} | Distance: {distance:.4f}")

    # Calculate summary statistics
    summary = calculate_summary(results, error_rates)

    return ExperimentResult(
        timestamp=datetime.now().isoformat(),
        test_sentences=sentences,
        sentence_lengths=[len(s.split()) for s in sentences],
        error_rates=error_rates,
        results=results,
        summary=summary
    )


def calculate_summary(results: List[TranslationResult],
                     error_rates: List[float]) -> Dict:
    """Calculate summary statistics from results."""
    summary = {
        'total_runs': len(results),
        'by_error_rate': {}
    }

    for rate in error_rates:
        rate_results = [r for r in results if abs(r.error_rate - rate) < 0.001]
        if rate_results:
            distances = [r.vector_distance for r in rate_results]
            similarities = [r.similarity_score for r in rate_results]
            summary['by_error_rate'][f'{rate*100:.0f}%'] = {
                'count': len(rate_results),
                'avg_distance': sum(distances) / len(distances),
                'avg_similarity': sum(similarities) / len(similarities),
                'min_distance': min(distances),
                'max_distance': max(distances)
            }

    return summary


# ============================================================================
# GRAPH GENERATION
# ============================================================================

def generate_graph(experiment: ExperimentResult, output_path: str = None) -> str:
    """
    Generate a graph showing spelling error % vs vector distance.

    Args:
        experiment: ExperimentResult from run_experiment()
        output_path: Path to save the graph (default: auto-generated)

    Returns:
        Path to saved graph
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend for servers
    except ImportError:
        raise ImportError("Please install matplotlib: pip install matplotlib")

    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(
            os.path.dirname(__file__),
            f"spelling_error_graph_{timestamp}.png"
        )

    # Extract data points
    error_rates = []
    distances = []
    similarities = []

    for result in experiment.results:
        error_rates.append(result.error_rate * 100)  # Convert to percentage
        distances.append(result.vector_distance)
        similarities.append(result.similarity_score)

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Spelling Error % vs Vector Distance
    ax1.scatter(error_rates, distances, alpha=0.6, s=100, c='blue', edgecolors='black')

    # Calculate and plot trend line
    if len(error_rates) > 1:
        z = np.polyfit(error_rates, distances, 1) if 'np' in dir() else None
        if z is not None:
            p = np.poly1d(z)
            x_line = sorted(set(error_rates))
            ax1.plot(x_line, [p(x) for x in x_line], "r--", alpha=0.8, label='Trend')

    # Calculate average per error rate
    rate_avg = {}
    for rate, dist in zip(error_rates, distances):
        if rate not in rate_avg:
            rate_avg[rate] = []
        rate_avg[rate].append(dist)

    avg_rates = sorted(rate_avg.keys())
    avg_distances = [sum(rate_avg[r])/len(rate_avg[r]) for r in avg_rates]
    ax1.plot(avg_rates, avg_distances, 'g-o', linewidth=2, markersize=8,
             label='Average', alpha=0.8)

    ax1.set_xlabel('Spelling Error Percentage (%)', fontsize=12)
    ax1.set_ylabel('Vector Distance (1 - Cosine Similarity)', fontsize=12)
    ax1.set_title('Spelling Error Rate vs. Translation Vector Distance', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(-5, 55)

    # Plot 2: Spelling Error % vs Similarity Score
    ax2.scatter(error_rates, similarities, alpha=0.6, s=100, c='green', edgecolors='black')

    # Average line for similarity
    avg_similarities = [sum([s for r, s in zip(error_rates, similarities) if r == rate])/
                       len([s for r, s in zip(error_rates, similarities) if r == rate])
                       for rate in avg_rates]
    ax2.plot(avg_rates, avg_similarities, 'b-o', linewidth=2, markersize=8,
             label='Average', alpha=0.8)

    ax2.set_xlabel('Spelling Error Percentage (%)', fontsize=12)
    ax2.set_ylabel('Cosine Similarity Score', fontsize=12)
    ax2.set_title('Spelling Error Rate vs. Semantic Similarity', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(-5, 55)
    ax2.set_ylim(0, 1.05)

    # Add quality threshold line
    ax2.axhline(y=0.85, color='orange', linestyle='--', alpha=0.7, label='Good threshold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nGraph saved to: {output_path}")
    return output_path


# ============================================================================
# RESULTS EXPORT
# ============================================================================

def save_results(experiment: ExperimentResult, output_path: str = None) -> str:
    """Save experiment results to JSON file."""
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(
            os.path.dirname(__file__),
            f"experiment_results_{timestamp}.json"
        )

    # Convert to serializable format
    data = {
        'timestamp': experiment.timestamp,
        'test_sentences': experiment.test_sentences,
        'sentence_lengths': experiment.sentence_lengths,
        'error_rates': experiment.error_rates,
        'results': [asdict(r) for r in experiment.results],
        'summary': experiment.summary
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Results saved to: {output_path}")
    return output_path


def print_deliverables(experiment: ExperimentResult):
    """Print assignment deliverables in formatted output."""
    print("\n" + "=" * 70)
    print("ASSIGNMENT DELIVERABLES")
    print("=" * 70)

    # 1. Sentences used
    print("\n1. TEST SENTENCES USED:")
    print("-" * 40)
    for i, sent in enumerate(experiment.test_sentences):
        print(f"\n   Sentence {i+1}:")
        print(f"   Original: {sent}")
        print(f"   Length: {experiment.sentence_lengths[i]} words")

    # Show misspelled versions
    print("\n   Misspelled versions by error rate:")
    seen = set()
    for result in experiment.results:
        key = (result.original_sentence[:50], result.error_rate)
        if key not in seen:
            seen.add(key)
            if result.error_rate > 0:
                print(f"   - {result.error_rate*100:.0f}%: {result.input_with_errors[:70]}...")

    # 2. Sentence lengths
    print("\n\n2. SENTENCE LENGTHS:")
    print("-" * 40)
    for i, length in enumerate(experiment.sentence_lengths):
        print(f"   Sentence {i+1}: {length} words")

    # 3. Summary statistics
    print("\n\n3. RESULTS SUMMARY:")
    print("-" * 40)
    print(f"\n   {'Error Rate':<15} {'Avg Distance':<15} {'Avg Similarity':<15}")
    print(f"   {'-'*45}")
    for rate, stats in experiment.summary['by_error_rate'].items():
        print(f"   {rate:<15} {stats['avg_distance']:<15.4f} {stats['avg_similarity']:<15.4f}")

    # 4. Graph info
    print("\n\n4. GRAPH:")
    print("-" * 40)
    print("   Graph will be generated as: spelling_error_graph_TIMESTAMP.png")
    print("   X-axis: Spelling error percentage (0% - 50%)")
    print("   Y-axis: Vector distance between original and final sentences")

    print("\n" + "=" * 70)


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Run translation quality experiment with spelling errors"
    )
    parser.add_argument('--mock', action='store_true',
                       help='Use mock translations instead of Claude API')
    parser.add_argument('--sentences-only', action='store_true',
                       help='Only display test sentences, do not run experiment')
    parser.add_argument('--api-key', type=str, default=None,
                       help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
    parser.add_argument('--output-dir', type=str, default=None,
                       help='Output directory for results')

    args = parser.parse_args()

    # Show sentences only
    if args.sentences_only:
        print("\n" + "=" * 70)
        print("TEST SENTENCES (15+ words each)")
        print("=" * 70)
        for i, sent in enumerate(TEST_SENTENCES):
            words = sent.split()
            print(f"\nSentence {i+1} ({len(words)} words):")
            print(f"  {sent}")
        return

    # Run full experiment
    print("\nStarting experiment...")
    experiment = run_experiment(
        use_mock=args.mock,
        api_key=args.api_key,
        verbose=True
    )

    # Print deliverables
    print_deliverables(experiment)

    # Save results
    save_results(experiment)

    # Generate graph
    try:
        generate_graph(experiment)
    except ImportError as e:
        print(f"\nWarning: Could not generate graph: {e}")
        print("Install matplotlib: pip install matplotlib")

    print("\nExperiment complete!")


if __name__ == "__main__":
    main()
