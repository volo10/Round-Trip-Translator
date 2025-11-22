#!/usr/bin/env python3
"""
Local Embedding Similarity Checker for Translation Quality Assessment

This script takes two sentences (input and output from the translation agents)
and embeds them using a local sentence transformer model, then computes the
cosine similarity between the vectors to assess semantic similarity.

No API key required - uses local models!

Usage:
    python3 embedding_similarity_local.py "original sentence" "translated sentence"

    Or interactively:
    python3 embedding_similarity_local.py
"""

import sys
import os
import math
from typing import List, Tuple
import json
from datetime import datetime

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Error: sentence-transformers package not installed.")
    print("Install with: python3 -m pip install sentence-transformers")
    sys.exit(1)


class LocalEmbeddingSimilarityChecker:
    """Check semantic similarity between two sentences using local embeddings."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding checker with a local model.

        Args:
            model_name: The sentence-transformers model to use
                       (default: all-MiniLM-L6-v2 - small and fast)
                       Other options: 'all-mpnet-base-v2' (more accurate, larger)
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.model_name = model_name
        self.input_sentence = None
        self.output_sentence = None
        self.input_embedding = None
        self.output_embedding = None
        self.similarity_score = None
        print("Model loaded successfully\n")

    def get_embedding(self, text: str) -> List[float]:
        """
        Get embedding for a sentence using the local model.

        Args:
            text: The text to embed

        Returns:
            List of floats representing the embedding vector
        """
        embeddings = self.model.encode([text], convert_to_numpy=True)
        return embeddings[0].tolist()

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculate cosine similarity between two vectors.

        Args:
            vec1: First embedding vector
            vec2: Second embedding vector

        Returns:
            Cosine similarity score between -1 and 1
        """
        # Calculate dot product
        dot_product = sum(a * b for a, b in zip(vec1, vec2))

        # Calculate magnitudes
        mag1 = math.sqrt(sum(a * a for a in vec1))
        mag2 = math.sqrt(sum(b * b for b in vec2))

        # Avoid division by zero
        if mag1 == 0 or mag2 == 0:
            return 0.0

        # Calculate and return cosine similarity
        return dot_product / (mag1 * mag2)

    def analyze(self, input_sentence: str, output_sentence: str) -> dict:
        """
        Analyze similarity between input and output sentences.

        Args:
            input_sentence: The original sentence (input to translation)
            output_sentence: The translated sentence (output from translation)

        Returns:
            Dictionary with analysis results
        """
        self.input_sentence = input_sentence
        self.output_sentence = output_sentence

        print("\n" + "="*70)
        print("  EMBEDDING SIMILARITY ANALYSIS (Local Model)")
        print("="*70)
        print()
        print(f"Input Sentence:  {input_sentence}")
        print(f"Output Sentence: {output_sentence}")
        print()

        # Get embeddings
        print("Generating embeddings...")
        print("  Embedding input sentence...")
        self.input_embedding = self.get_embedding(input_sentence)
        print(f"  Input embedding generated ({len(self.input_embedding)} dimensions)")

        print("  Embedding output sentence...")
        self.output_embedding = self.get_embedding(output_sentence)
        print(f"  ✓ Output embedding generated ({len(self.output_embedding)} dimensions)")

        # Calculate similarity
        print()
        print("Computing similarity...")
        self.similarity_score = self.cosine_similarity(
            self.input_embedding,
            self.output_embedding
        )
        print(f"  ✓ Similarity calculated")

        # Create results dictionary
        results = {
            "input_sentence": input_sentence,
            "output_sentence": output_sentence,
            "similarity_score": self.similarity_score,
            "embedding_model": self.model_name,
            "embedding_dimensions": len(self.input_embedding),
            "timestamp": datetime.now().isoformat()
        }

        # Add interpretation
        results["interpretation"] = self._interpret_score(self.similarity_score)

        return results

    def _interpret_score(self, score: float) -> str:
        """
        Interpret the similarity score.

        Args:
            score: Cosine similarity score between -1 and 1

        Returns:
            String interpretation of the score
        """
        if score >= 0.95:
            return "Identical/Near-Identical (semantically the same)"
        elif score >= 0.85:
            return "Very Similar (same core meaning)"
        elif score >= 0.75:
            return "Similar (comparable meanings)"
        elif score >= 0.65:
            return "Moderately Similar (related concepts)"
        elif score >= 0.50:
            return "Somewhat Similar (some semantic overlap)"
        elif score >= 0.30:
            return "Weakly Similar (minimal semantic overlap)"
        else:
            return "Dissimilar (different meanings)"

    def print_results(self, results: dict) -> None:
        """
        Print formatted results.

        Args:
            results: Results dictionary from analyze()
        """
        print()
        print("="*70)
        print("  RESULTS")
        print("="*70)
        print()
        print(f"Input:  {results['input_sentence']}")
        print(f"Output: {results['output_sentence']}")
        print()
        print(f"Similarity Score: {results['similarity_score']:.4f}")
        print(f"Interpretation:   {results['interpretation']}")
        print()
        print(f"Embedding Model:  {results['embedding_model']}")
        print(f"Dimensions:       {results['embedding_dimensions']}")
        print()
        print("="*70)
        print()

        # Quality assessment for translation
        score = results['similarity_score']
        if score >= 0.85:
            print("✓ Translation Quality: EXCELLENT")
            print("  The output sentence preserves the semantic meaning of the input.")
        elif score >= 0.75:
            print("✓ Translation Quality: GOOD")
            print("  The output sentence maintains similar semantic meaning.")
        elif score >= 0.65:
            print("⚠ Translation Quality: FAIR")
            print("  The output sentence has some semantic drift from the input.")
        elif score >= 0.50:
            print("⚠ Translation Quality: POOR")
            print("  The output sentence has significant semantic differences.")
        else:
            print("✗ Translation Quality: VERY POOR")
            print("  The output sentence differs substantially from the input.")

        print()
        print("="*70)
        print()

    def save_results(self, results: dict, filename: str = None) -> str:
        """
        Save results to a JSON file.

        Args:
            results: Results dictionary from analyze()
            filename: Optional custom filename

        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"embedding_similarity_{timestamp}.json"

        filepath = os.path.join(os.path.dirname(__file__), filename)

        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"Results saved to: {filepath}")
        return filepath


def main():
    """Main entry point for the script."""

    # Check for command line arguments
    if len(sys.argv) == 3:
        # Use command line arguments
        input_sentence = sys.argv[1]
        output_sentence = sys.argv[2]
    elif len(sys.argv) == 1:
        # Interactive mode
        print("\n" + "="*70)
        print("  EMBEDDING SIMILARITY CHECKER (Local Model)")
        print("="*70)
        print()
        print("Enter two sentences to compare their semantic similarity.")
        print("(These are typically the input and output of translation agents)")
        print()

        input_sentence = input("Input Sentence:  ").strip()
        if not input_sentence:
            print("Error: Input sentence cannot be empty")
            sys.exit(1)

        output_sentence = input("Output Sentence: ").strip()
        if not output_sentence:
            print("Error: Output sentence cannot be empty")
            sys.exit(1)
    else:
        print("Usage: python3 embedding_similarity_local.py [input_sentence] [output_sentence]")
        print()
        print("Examples:")
        print('  python3 embedding_similarity_local.py "I like going to the beach" "I love going to the beach"')
        print('  python3 embedding_similarity_local.py (for interactive mode)')
        print()
        print("Note: Requires sentence-transformers library")
        print("Install with: python3 -m pip install sentence-transformers")
        sys.exit(1)

    # Initialize checker
    try:
        print("\nInitializing embedding similarity checker...")
        checker = LocalEmbeddingSimilarityChecker()
    except Exception as e:
        print(f"Error: Could not initialize embedding model.")
        print(f"Details: {e}")
        print()
        print("Install required package with:")
        print("  python3 -m pip install sentence-transformers")
        sys.exit(1)

    # Analyze
    try:
        results = checker.analyze(input_sentence, output_sentence)
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)

    # Print and save results
    checker.print_results(results)
    checker.save_results(results)


if __name__ == "__main__":
    main()
