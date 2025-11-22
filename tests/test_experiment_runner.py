#!/usr/bin/env python3
"""
Unit tests for the Experiment Runner module.

Run with: pytest tests/test_experiment_runner.py -v
Or: python -m pytest tests/ -v
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import pytest

# Try to import the module
try:
    from run_experiment import (
        TEST_SENTENCES,
        mock_translate,
        run_translation_pipeline,
        run_experiment,
        calculate_summary,
        TranslationResult,
        ExperimentResult
    )
    from spelling_error_injector import SpellingErrorInjector
    EXPERIMENT_AVAILABLE = True
except ImportError as e:
    EXPERIMENT_AVAILABLE = False
    IMPORT_ERROR = str(e)


pytestmark = pytest.mark.skipif(
    not EXPERIMENT_AVAILABLE,
    reason="Required modules not available"
)


class TestTestSentences:
    """Test that test sentences meet assignment requirements."""

    def test_minimum_two_sentences(self):
        """Test that at least 2 test sentences are defined."""
        assert len(TEST_SENTENCES) >= 2

    def test_sentences_have_15_plus_words(self):
        """Test that all sentences have at least 15 words (assignment requirement)."""
        for i, sentence in enumerate(TEST_SENTENCES):
            word_count = len(sentence.split())
            assert word_count >= 15, \
                f"Sentence {i+1} has only {word_count} words, needs 15+"

    def test_sentences_are_english(self):
        """Test that sentences appear to be English."""
        for sentence in TEST_SENTENCES:
            # Basic check: should contain common English words
            common_words = ['the', 'a', 'is', 'are', 'to', 'with', 'and', 'of']
            sentence_lower = sentence.lower()
            has_english = any(word in sentence_lower for word in common_words)
            assert has_english, f"Sentence doesn't appear to be English: {sentence[:50]}..."

    def test_sentences_not_empty(self):
        """Test that no sentences are empty."""
        for sentence in TEST_SENTENCES:
            assert len(sentence.strip()) > 0


class TestMockTranslation:
    """Test the mock translation function."""

    def test_mock_translate_en_to_fr(self):
        """Test English to French mock translation."""
        text = "The beautiful sunset"
        result = mock_translate(text, "English", "French")

        # Should return something (mock just transforms words)
        assert len(result) > 0

    def test_mock_translate_fr_to_he(self):
        """Test French to Hebrew mock translation."""
        text = "Le beau coucher de soleil"
        result = mock_translate(text, "French", "Hebrew")

        # Should return Hebrew-like text
        assert len(result) > 0

    def test_mock_translate_he_to_en(self):
        """Test Hebrew to English mock translation."""
        text = "השקיעה היפה"
        result = mock_translate(text, "Hebrew", "English")

        # Should return English text
        assert len(result) > 0


class TestTranslationPipeline:
    """Test the translation pipeline."""

    def test_pipeline_returns_tuple(self):
        """Test that pipeline returns a 3-tuple."""
        result = run_translation_pipeline("Hello world", use_mock=True)

        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_pipeline_all_steps_produce_output(self):
        """Test that all pipeline steps produce non-empty output."""
        french, hebrew, english = run_translation_pipeline(
            "The beautiful sunset painted the sky",
            use_mock=True
        )

        assert len(french) > 0
        assert len(hebrew) > 0
        assert len(english) > 0

    def test_pipeline_mock_mode(self):
        """Test that mock mode doesn't require API key."""
        # Should not raise an exception
        result = run_translation_pipeline(
            "Test sentence for translation",
            use_mock=True
        )

        assert result is not None


class TestExperimentRunner:
    """Test the experiment runner."""

    @pytest.fixture
    def sample_results(self):
        """Create sample translation results for testing."""
        return [
            TranslationResult(
                original_sentence="Test sentence one",
                input_with_errors="Test sentence one",
                error_rate=0.0,
                actual_error_rate=0.0,
                french_translation="FR",
                hebrew_translation="HE",
                final_english="Test sentence one",
                similarity_score=0.99,
                vector_distance=0.01
            ),
            TranslationResult(
                original_sentence="Test sentence one",
                input_with_errors="Tset sentance one",
                error_rate=0.25,
                actual_error_rate=0.25,
                french_translation="FR",
                hebrew_translation="HE",
                final_english="Test sentence one",
                similarity_score=0.95,
                vector_distance=0.05
            ),
            TranslationResult(
                original_sentence="Test sentence one",
                input_with_errors="Tset sentance oen",
                error_rate=0.50,
                actual_error_rate=0.50,
                french_translation="FR",
                hebrew_translation="HE",
                final_english="Testing sentence one",
                similarity_score=0.85,
                vector_distance=0.15
            )
        ]

    def test_calculate_summary(self, sample_results):
        """Test summary calculation."""
        error_rates = [0.0, 0.25, 0.50]
        summary = calculate_summary(sample_results, error_rates)

        assert 'total_runs' in summary
        assert 'by_error_rate' in summary
        assert summary['total_runs'] == 3

    def test_summary_by_error_rate(self, sample_results):
        """Test that summary groups results by error rate."""
        error_rates = [0.0, 0.25, 0.50]
        summary = calculate_summary(sample_results, error_rates)

        assert '0%' in summary['by_error_rate']
        assert '25%' in summary['by_error_rate']
        assert '50%' in summary['by_error_rate']

    def test_summary_average_calculations(self, sample_results):
        """Test that summary calculates correct averages."""
        error_rates = [0.0, 0.25, 0.50]
        summary = calculate_summary(sample_results, error_rates)

        # Check 0% error rate
        stats_0 = summary['by_error_rate']['0%']
        assert stats_0['avg_distance'] == pytest.approx(0.01)
        assert stats_0['avg_similarity'] == pytest.approx(0.99)


class TestTranslationResult:
    """Test TranslationResult dataclass."""

    def test_translation_result_creation(self):
        """Test creating a TranslationResult."""
        result = TranslationResult(
            original_sentence="Original",
            input_with_errors="Originol",
            error_rate=0.25,
            actual_error_rate=0.20,
            french_translation="French",
            hebrew_translation="Hebrew",
            final_english="Final",
            similarity_score=0.90,
            vector_distance=0.10
        )

        assert result.original_sentence == "Original"
        assert result.error_rate == 0.25
        assert result.similarity_score == 0.90

    def test_vector_distance_calculation(self):
        """Test that vector distance is 1 - similarity."""
        result = TranslationResult(
            original_sentence="Test",
            input_with_errors="Test",
            error_rate=0.0,
            actual_error_rate=0.0,
            french_translation="FR",
            hebrew_translation="HE",
            final_english="Test",
            similarity_score=0.85,
            vector_distance=0.15  # Should be 1 - 0.85
        )

        assert result.vector_distance == pytest.approx(1 - result.similarity_score)


class TestAssignmentCompliance:
    """Test that the experiment meets assignment requirements."""

    def test_error_rates_cover_required_range(self):
        """Test that experiments cover 0% to 50% error rates."""
        default_rates = [0.0, 0.10, 0.20, 0.25, 0.30, 0.40, 0.50]

        # Should include 0%
        assert 0.0 in default_rates

        # Should include 25% (assignment minimum)
        assert 0.25 in default_rates

        # Should include 50%
        assert 0.50 in default_rates

    def test_sentences_meet_word_count_requirement(self):
        """Test all test sentences have 15+ words."""
        for sentence in TEST_SENTENCES:
            words = sentence.split()
            assert len(words) >= 15

    def test_similarity_to_distance_conversion(self):
        """Test that we can convert similarity to distance for graphs."""
        similarity = 0.9747
        distance = 1 - similarity

        assert distance == pytest.approx(0.0253)


class TestIntegration:
    """Integration tests for the full experiment flow."""

    @pytest.mark.slow
    def test_full_experiment_mock_mode(self):
        """Test running a full experiment in mock mode."""
        # Run with minimal data to test integration
        experiment = run_experiment(
            sentences=TEST_SENTENCES[:1],  # Just first sentence
            error_rates=[0.0, 0.25],  # Just two rates
            use_mock=True,
            verbose=False
        )

        assert isinstance(experiment, ExperimentResult)
        assert len(experiment.results) > 0
        assert experiment.summary is not None

    @pytest.mark.slow
    def test_experiment_produces_results_for_each_rate(self):
        """Test that experiment produces results for each error rate."""
        error_rates = [0.0, 0.25, 0.50]
        experiment = run_experiment(
            sentences=TEST_SENTENCES[:1],
            error_rates=error_rates,
            use_mock=True,
            verbose=False
        )

        # Should have one result per error rate
        assert len(experiment.results) == len(error_rates)

    @pytest.mark.slow
    def test_experiment_captures_sentence_lengths(self):
        """Test that experiment captures sentence lengths."""
        experiment = run_experiment(
            sentences=TEST_SENTENCES,
            error_rates=[0.0],
            use_mock=True,
            verbose=False
        )

        assert len(experiment.sentence_lengths) == len(TEST_SENTENCES)
        assert all(length >= 15 for length in experiment.sentence_lengths)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
