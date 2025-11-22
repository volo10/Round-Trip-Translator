#!/usr/bin/env python3
"""
Unit tests for the Spelling Error Injector module.

Run with: pytest tests/test_spelling_error_injector.py -v
Or: python -m pytest tests/ -v
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import pytest
from spelling_error_injector import SpellingErrorInjector, ErrorStats


class TestSpellingErrorInjector:
    """Test suite for SpellingErrorInjector class."""

    @pytest.fixture
    def injector(self):
        """Create an injector with fixed seed for reproducibility."""
        return SpellingErrorInjector(seed=42)

    @pytest.fixture
    def sample_sentence(self):
        """Sample sentence with 15+ words."""
        return "The quick brown fox jumps over the lazy dog while beautiful sunset paints the sky with colors"

    # =========================================================================
    # Basic Functionality Tests
    # =========================================================================

    def test_injector_initialization(self, injector):
        """Test that injector initializes correctly."""
        assert injector is not None
        assert injector.rng is not None

    def test_zero_error_rate_returns_original(self, injector, sample_sentence):
        """Test that 0% error rate returns the original text unchanged."""
        result = injector.inject_errors(sample_sentence, error_rate=0.0)

        assert result.modified_text == sample_sentence
        assert result.words_modified == 0
        assert result.actual_error_rate == 0.0

    def test_error_stats_structure(self, injector, sample_sentence):
        """Test that ErrorStats contains all required fields."""
        result = injector.inject_errors(sample_sentence, error_rate=0.25)

        assert isinstance(result, ErrorStats)
        assert hasattr(result, 'original_text')
        assert hasattr(result, 'modified_text')
        assert hasattr(result, 'total_words')
        assert hasattr(result, 'words_modified')
        assert hasattr(result, 'actual_error_rate')
        assert hasattr(result, 'target_error_rate')
        assert hasattr(result, 'modifications')

    def test_original_text_preserved(self, injector, sample_sentence):
        """Test that original text is stored correctly."""
        result = injector.inject_errors(sample_sentence, error_rate=0.30)

        assert result.original_text == sample_sentence

    # =========================================================================
    # Error Rate Tests
    # =========================================================================

    def test_error_rate_25_percent(self, injector, sample_sentence):
        """Test that ~25% of words are modified at 25% error rate."""
        result = injector.inject_errors(sample_sentence, error_rate=0.25)

        # Should modify approximately 25% of eligible words
        assert result.words_modified > 0
        assert result.actual_error_rate <= 0.30  # Allow some variance

    def test_error_rate_50_percent(self, injector, sample_sentence):
        """Test that ~50% of words are modified at 50% error rate."""
        result = injector.inject_errors(sample_sentence, error_rate=0.50)

        # Should modify approximately 50% of eligible words
        assert result.words_modified > 0
        assert result.actual_error_rate > 0.20  # Should be significant

    def test_increasing_error_rates(self, injector, sample_sentence):
        """Test that higher error rates produce more modifications."""
        result_10 = injector.inject_errors(sample_sentence, error_rate=0.10)
        # Reset RNG
        injector.rng.seed(42)
        result_50 = injector.inject_errors(sample_sentence, error_rate=0.50)

        assert result_50.words_modified >= result_10.words_modified

    def test_invalid_error_rate_raises(self, injector, sample_sentence):
        """Test that invalid error rates raise ValueError."""
        with pytest.raises(ValueError):
            injector.inject_errors(sample_sentence, error_rate=-0.1)

        with pytest.raises(ValueError):
            injector.inject_errors(sample_sentence, error_rate=1.5)

    # =========================================================================
    # Word Modification Tests
    # =========================================================================

    def test_short_words_not_modified(self, injector):
        """Test that very short words (< 3 chars) are not modified."""
        text = "I am a to be or in on"  # All short words
        result = injector.inject_errors(text, error_rate=1.0)

        # Very short words should be skipped
        assert result.words_modified == 0

    def test_numbers_not_modified(self, injector):
        """Test that numbers are not modified."""
        text = "There are 123 and 456 items here today"
        result = injector.inject_errors(text, error_rate=1.0)

        # Check that numbers remain unchanged
        assert "123" in result.modified_text
        assert "456" in result.modified_text

    def test_modifications_tracked(self, injector, sample_sentence):
        """Test that modifications are properly tracked."""
        result = injector.inject_errors(sample_sentence, error_rate=0.30)

        assert len(result.modifications) == result.words_modified

        # Each modification should be a tuple of (original, modified)
        for orig, mod in result.modifications:
            assert isinstance(orig, str)
            assert isinstance(mod, str)
            assert orig != mod  # Should be different

    def test_word_count_preserved(self, injector, sample_sentence):
        """Test that word count is preserved after injection."""
        result = injector.inject_errors(sample_sentence, error_rate=0.30)

        original_count = len(sample_sentence.split())
        modified_count = len(result.modified_text.split())

        assert modified_count == original_count

    # =========================================================================
    # Reproducibility Tests
    # =========================================================================

    def test_same_seed_produces_same_results(self):
        """Test that same seed produces identical results."""
        text = "The beautiful sunset painted the sky with vibrant colors"

        injector1 = SpellingErrorInjector(seed=123)
        result1 = injector1.inject_errors(text, error_rate=0.30)

        injector2 = SpellingErrorInjector(seed=123)
        result2 = injector2.inject_errors(text, error_rate=0.30)

        assert result1.modified_text == result2.modified_text
        assert result1.modifications == result2.modifications

    def test_different_seeds_produce_different_results(self):
        """Test that different seeds can produce different results."""
        text = "The beautiful sunset painted the sky with vibrant colors"

        injector1 = SpellingErrorInjector(seed=123)
        result1 = injector1.inject_errors(text, error_rate=0.50)

        injector2 = SpellingErrorInjector(seed=456)
        result2 = injector2.inject_errors(text, error_rate=0.50)

        # High probability of difference with 50% error rate
        # (but not guaranteed, so we just check they're both valid)
        assert result1.modified_text != text or result2.modified_text != text

    # =========================================================================
    # Generate Variants Tests
    # =========================================================================

    def test_generate_variants_default_rates(self, injector, sample_sentence):
        """Test generate_error_variants with default rates."""
        variants = injector.generate_error_variants(sample_sentence)

        # Default rates: 0%, 10%, 20%, 25%, 30%, 40%, 50%
        assert len(variants) == 7

        # First variant (0%) should be unchanged
        assert variants[0].modified_text == sample_sentence

    def test_generate_variants_custom_rates(self, injector, sample_sentence):
        """Test generate_error_variants with custom rates."""
        custom_rates = [0.0, 0.25, 0.50]
        variants = injector.generate_error_variants(sample_sentence, error_rates=custom_rates)

        assert len(variants) == len(custom_rates)

        for variant, rate in zip(variants, custom_rates):
            assert variant.target_error_rate == rate

    # =========================================================================
    # Edge Cases
    # =========================================================================

    def test_empty_string(self, injector):
        """Test handling of empty string."""
        result = injector.inject_errors("", error_rate=0.25)

        assert result.modified_text == ""
        assert result.total_words == 0
        assert result.words_modified == 0

    def test_single_word(self, injector):
        """Test handling of single word."""
        result = injector.inject_errors("Hello", error_rate=0.25)

        assert result.total_words == 1

    def test_punctuation_preserved(self, injector):
        """Test that punctuation at end of words is preserved."""
        text = "Hello, world! How are you?"
        result = injector.inject_errors(text, error_rate=0.50)

        # Check that sentences still have proper punctuation structure
        assert result.modified_text.count(',') == text.count(',')
        assert result.modified_text.count('!') == text.count('!')
        assert result.modified_text.count('?') == text.count('?')

    def test_case_preservation(self, injector):
        """Test that capitalization pattern is roughly preserved."""
        text = "The QUICK Brown FOX"
        result = injector.inject_errors(text, error_rate=0.50)

        # First word should still start with capital
        words = result.modified_text.split()
        assert words[0][0].isupper()


class TestErrorStatistics:
    """Test suite for error statistics calculations."""

    @pytest.fixture
    def injector(self):
        return SpellingErrorInjector(seed=42)

    def test_actual_error_rate_calculation(self, injector):
        """Test that actual error rate is correctly calculated."""
        text = "one two three four five six seven eight nine ten"  # 10 words
        result = injector.inject_errors(text, error_rate=0.30)

        expected_rate = result.words_modified / result.total_words
        assert abs(result.actual_error_rate - expected_rate) < 0.001

    def test_total_words_count(self, injector):
        """Test that total words is correctly counted."""
        text = "This sentence has exactly seven words here"
        result = injector.inject_errors(text, error_rate=0.0)

        assert result.total_words == 7


class TestAssignmentRequirements:
    """Test that implementation meets assignment requirements."""

    @pytest.fixture
    def injector(self):
        return SpellingErrorInjector(seed=42)

    def test_15_plus_word_sentence(self, injector):
        """Test with a sentence of 15+ words as required by assignment."""
        sentence = ("The magnificent golden sunset painted the entire western sky "
                   "with beautiful shades of orange pink and purple colors")
        word_count = len(sentence.split())

        assert word_count >= 15, f"Test sentence should have 15+ words, has {word_count}"

        result = injector.inject_errors(sentence, error_rate=0.25)

        # At 25% error rate, should modify at least some words
        assert result.words_modified > 0
        assert result.actual_error_rate >= 0.15  # Allow some variance

    def test_25_percent_minimum_errors(self, injector):
        """Test that 25% error injection works as required."""
        sentence = ("Every morning the dedicated young student walks through "
                   "the peaceful park to reach her university campus on time")

        result = injector.inject_errors(sentence, error_rate=0.25)

        # Should have approximately 25% errors
        assert result.target_error_rate == 0.25
        assert result.words_modified > 0

    def test_error_range_0_to_50(self, injector):
        """Test error injection across 0% to 50% range."""
        sentence = ("The beautiful morning sunshine illuminated the entire garden "
                   "with warm golden rays of light streaming through the trees")

        error_rates = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50]

        for rate in error_rates:
            injector.rng.seed(42)  # Reset for consistency
            result = injector.inject_errors(sentence, error_rate=rate)

            assert result.target_error_rate == rate
            if rate == 0.0:
                assert result.words_modified == 0
            elif rate >= 0.20:
                assert result.words_modified > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
