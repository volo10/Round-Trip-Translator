#!/usr/bin/env python3
"""
Unit tests for the Embedding Similarity Checker module.

Run with: pytest tests/test_embedding_similarity.py -v
Or: python -m pytest tests/ -v

Note: These tests require sentence-transformers to be installed.
Some tests are marked as slow due to model loading time.
"""

import sys
import os
import math
import tempfile

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import pytest

# Try to import the module, skip tests if dependencies not available
try:
    from embedding_similarity_local import LocalEmbeddingSimilarityChecker
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    EMBEDDINGS_AVAILABLE = False


# Skip all tests if sentence-transformers not installed
pytestmark = pytest.mark.skipif(
    not EMBEDDINGS_AVAILABLE,
    reason="sentence-transformers not installed"
)


class TestLocalEmbeddingSimilarityChecker:
    """Test suite for LocalEmbeddingSimilarityChecker class."""

    @pytest.fixture(scope="class")
    def checker(self):
        """Create a checker instance (cached for class to avoid repeated model loading)."""
        return LocalEmbeddingSimilarityChecker()

    # =========================================================================
    # Initialization Tests
    # =========================================================================

    def test_checker_initialization(self, checker):
        """Test that checker initializes correctly."""
        assert checker is not None
        assert checker.model is not None
        assert checker.model_name == "all-MiniLM-L6-v2"

    def test_default_model_name(self, checker):
        """Test that default model is all-MiniLM-L6-v2."""
        assert checker.model_name == "all-MiniLM-L6-v2"

    # =========================================================================
    # Embedding Tests
    # =========================================================================

    def test_get_embedding_returns_list(self, checker):
        """Test that get_embedding returns a list of floats."""
        embedding = checker.get_embedding("Hello world")

        assert isinstance(embedding, list)
        assert len(embedding) > 0
        assert all(isinstance(x, float) for x in embedding)

    def test_embedding_dimensions(self, checker):
        """Test that embeddings have expected dimensions (384 for MiniLM)."""
        embedding = checker.get_embedding("Test sentence")

        assert len(embedding) == 384

    def test_different_texts_different_embeddings(self, checker):
        """Test that different texts produce different embeddings."""
        emb1 = checker.get_embedding("The cat sat on the mat")
        emb2 = checker.get_embedding("Quantum physics is complex")

        # Embeddings should be different
        assert emb1 != emb2

    def test_similar_texts_similar_embeddings(self, checker):
        """Test that similar texts produce similar embeddings."""
        emb1 = checker.get_embedding("I like going to the beach")
        emb2 = checker.get_embedding("I love going to the beach")

        # Calculate cosine similarity manually
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        mag1 = math.sqrt(sum(a * a for a in emb1))
        mag2 = math.sqrt(sum(b * b for b in emb2))
        similarity = dot_product / (mag1 * mag2)

        # Should be highly similar
        assert similarity > 0.9

    # =========================================================================
    # Cosine Similarity Tests
    # =========================================================================

    def test_cosine_similarity_identical_vectors(self, checker):
        """Test that identical vectors have similarity 1.0."""
        vec = [1.0, 2.0, 3.0, 4.0]
        similarity = checker.cosine_similarity(vec, vec)

        assert abs(similarity - 1.0) < 0.0001

    def test_cosine_similarity_orthogonal_vectors(self, checker):
        """Test that orthogonal vectors have similarity 0.0."""
        vec1 = [1.0, 0.0, 0.0]
        vec2 = [0.0, 1.0, 0.0]
        similarity = checker.cosine_similarity(vec1, vec2)

        assert abs(similarity - 0.0) < 0.0001

    def test_cosine_similarity_opposite_vectors(self, checker):
        """Test that opposite vectors have similarity -1.0."""
        vec1 = [1.0, 2.0, 3.0]
        vec2 = [-1.0, -2.0, -3.0]
        similarity = checker.cosine_similarity(vec1, vec2)

        assert abs(similarity - (-1.0)) < 0.0001

    def test_cosine_similarity_zero_vector(self, checker):
        """Test handling of zero vector."""
        vec1 = [1.0, 2.0, 3.0]
        vec2 = [0.0, 0.0, 0.0]
        similarity = checker.cosine_similarity(vec1, vec2)

        assert similarity == 0.0

    # =========================================================================
    # Analysis Tests
    # =========================================================================

    def test_analyze_returns_dict(self, checker):
        """Test that analyze returns a dictionary."""
        result = checker.analyze("Hello", "Hello")

        assert isinstance(result, dict)

    def test_analyze_result_keys(self, checker):
        """Test that analyze result contains all required keys."""
        result = checker.analyze("Input text", "Output text")

        required_keys = [
            'input_sentence', 'output_sentence', 'similarity_score',
            'embedding_model', 'embedding_dimensions', 'timestamp',
            'interpretation'
        ]

        for key in required_keys:
            assert key in result, f"Missing key: {key}"

    def test_analyze_identical_sentences(self, checker):
        """Test that identical sentences have similarity ~1.0."""
        sentence = "The quick brown fox jumps over the lazy dog"
        result = checker.analyze(sentence, sentence)

        assert result['similarity_score'] > 0.99

    def test_analyze_similar_sentences(self, checker):
        """Test similarity of semantically similar sentences."""
        input_text = "I like going to the beach"
        output_text = "I love going to the beach"

        result = checker.analyze(input_text, output_text)

        # Should be very similar
        assert result['similarity_score'] > 0.90

    def test_analyze_different_sentences(self, checker):
        """Test similarity of semantically different sentences."""
        input_text = "The cat sleeps on the sofa"
        output_text = "Quantum mechanics describes particle behavior"

        result = checker.analyze(input_text, output_text)

        # Should have lower similarity
        assert result['similarity_score'] < 0.5

    # =========================================================================
    # Interpretation Tests
    # =========================================================================

    def test_interpret_excellent_score(self, checker):
        """Test interpretation of excellent similarity score."""
        interpretation = checker._interpret_score(0.97)
        assert "Identical" in interpretation or "Near-Identical" in interpretation

    def test_interpret_very_similar_score(self, checker):
        """Test interpretation of very similar score."""
        interpretation = checker._interpret_score(0.88)
        assert "Very Similar" in interpretation

    def test_interpret_similar_score(self, checker):
        """Test interpretation of similar score."""
        interpretation = checker._interpret_score(0.78)
        assert "Similar" in interpretation

    def test_interpret_moderately_similar_score(self, checker):
        """Test interpretation of moderately similar score."""
        interpretation = checker._interpret_score(0.68)
        assert "Moderately" in interpretation or "Similar" in interpretation

    def test_interpret_dissimilar_score(self, checker):
        """Test interpretation of dissimilar score."""
        interpretation = checker._interpret_score(0.20)
        assert "Dissimilar" in interpretation or "Weak" in interpretation

    # =========================================================================
    # Save Results Tests
    # =========================================================================

    def test_save_results_creates_file(self, checker):
        """Test that save_results creates a JSON file."""
        result = checker.analyze("Test input", "Test output")

        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            filepath = f.name

        try:
            saved_path = checker.save_results(result, filepath)
            assert os.path.exists(saved_path)

            # Verify it's valid JSON
            import json
            with open(saved_path) as f:
                loaded = json.load(f)

            assert 'similarity_score' in loaded
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)


class TestTranslationQualityThresholds:
    """Test quality thresholds for translation assessment."""

    @pytest.fixture(scope="class")
    def checker(self):
        return LocalEmbeddingSimilarityChecker()

    def test_excellent_translation_quality(self, checker):
        """Test that semantically identical translations score excellent."""
        original = "I like going to the beach with my friends"
        translated = "I love going to the beach with my friends"

        result = checker.analyze(original, translated)

        # Should exceed 0.85 threshold for "GOOD" quality
        assert result['similarity_score'] >= 0.85

    def test_good_translation_quality(self, checker):
        """Test that good translations meet threshold."""
        original = "The student walks to school every morning"
        translated = "Every morning the student goes to school"

        result = checker.analyze(original, translated)

        # Should be above 0.75 for acceptable
        assert result['similarity_score'] >= 0.75

    def test_assignment_threshold_compliance(self, checker):
        """Test that translation quality meets assignment requirements."""
        # Test case from assignment context
        original = "I like going to the beach with Ben"
        # Simulated translation output
        translated = "I love going to the beach with Ben"

        result = checker.analyze(original, translated)

        # Should exceed 0.85 threshold as per assignment standards
        assert result['similarity_score'] >= 0.85, \
            f"Translation quality {result['similarity_score']:.4f} below 0.85 threshold"


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.fixture(scope="class")
    def checker(self):
        return LocalEmbeddingSimilarityChecker()

    def test_empty_string_handling(self, checker):
        """Test handling of empty strings."""
        result = checker.analyze("", "")

        # Should handle gracefully
        assert 'similarity_score' in result

    def test_single_word_handling(self, checker):
        """Test handling of single words."""
        result = checker.analyze("Hello", "Hello")

        assert result['similarity_score'] > 0.99

    def test_unicode_handling(self, checker):
        """Test handling of Unicode characters."""
        result = checker.analyze(
            "The café serves délicious croissants",
            "The cafe serves delicious croissants"
        )

        # Should handle Unicode gracefully
        assert 'similarity_score' in result
        assert result['similarity_score'] > 0.8

    def test_long_text_handling(self, checker):
        """Test handling of longer texts."""
        long_text = " ".join(["The quick brown fox jumps over the lazy dog"] * 10)
        result = checker.analyze(long_text, long_text)

        assert result['similarity_score'] > 0.99

    def test_special_characters(self, checker):
        """Test handling of special characters."""
        result = checker.analyze(
            "Hello! How are you? I'm fine.",
            "Hello! How are you? I am fine."
        )

        assert 'similarity_score' in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
