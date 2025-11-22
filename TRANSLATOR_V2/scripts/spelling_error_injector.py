#!/usr/bin/env python3
"""
Spelling Error Injector for Translation Quality Experiments

This module provides functions to inject spelling errors into English text
at various error rates (0% to 50%) for testing translation pipeline robustness.

Usage:
    from spelling_error_injector import SpellingErrorInjector

    injector = SpellingErrorInjector(seed=42)
    misspelled = injector.inject_errors("Hello world", error_rate=0.25)
"""

import random
import string
from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ErrorStats:
    """Statistics about injected errors."""
    original_text: str
    modified_text: str
    total_words: int
    words_modified: int
    actual_error_rate: float
    target_error_rate: float
    modifications: List[Tuple[str, str]]  # (original, modified) pairs


class SpellingErrorInjector:
    """Inject spelling errors into text at configurable rates."""

    # Common spelling error patterns
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

    # Common letter substitutions (typos based on keyboard proximity)
    KEYBOARD_ADJACENT = {
        'q': ['w', 'a'], 'w': ['q', 'e', 's', 'a'], 'e': ['w', 'r', 'd', 's'],
        'r': ['e', 't', 'f', 'd'], 't': ['r', 'y', 'g', 'f'], 'y': ['t', 'u', 'h', 'g'],
        'u': ['y', 'i', 'j', 'h'], 'i': ['u', 'o', 'k', 'j'], 'o': ['i', 'p', 'l', 'k'],
        'p': ['o', 'l'],
        'a': ['q', 'w', 's', 'z'], 's': ['a', 'w', 'e', 'd', 'z', 'x'],
        'd': ['s', 'e', 'r', 'f', 'x', 'c'], 'f': ['d', 'r', 't', 'g', 'c', 'v'],
        'g': ['f', 't', 'y', 'h', 'v', 'b'], 'h': ['g', 'y', 'u', 'j', 'b', 'n'],
        'j': ['h', 'u', 'i', 'k', 'n', 'm'], 'k': ['j', 'i', 'o', 'l', 'm'],
        'l': ['k', 'o', 'p'],
        'z': ['a', 's', 'x'], 'x': ['z', 's', 'd', 'c'],
        'c': ['x', 'd', 'f', 'v'], 'v': ['c', 'f', 'g', 'b'],
        'b': ['v', 'g', 'h', 'n'], 'n': ['b', 'h', 'j', 'm'],
        'm': ['n', 'j', 'k']
    }

    # Common phonetic substitutions
    PHONETIC_SUBS = {
        'ph': 'f', 'f': 'ph',
        'ck': 'k', 'k': 'ck',
        'c': 's', 's': 'c',
        'ee': 'ea', 'ea': 'ee',
        'ie': 'ei', 'ei': 'ie',
        'ou': 'ow', 'ow': 'ou',
        'tion': 'shun', 'sion': 'shun',
    }

    def __init__(self, seed: Optional[int] = None):
        """
        Initialize the error injector.

        Args:
            seed: Random seed for reproducibility
        """
        self.rng = random.Random(seed)

    def _should_modify_word(self, word: str) -> bool:
        """Check if a word should be considered for modification."""
        # Skip very short words, numbers, punctuation-only
        if len(word) < 3:
            return False
        if word.isdigit():
            return False
        if not any(c.isalpha() for c in word):
            return False
        return True

    def _apply_error(self, word: str) -> str:
        """Apply a random spelling error to a word."""
        if len(word) < 2:
            return word

        # Extract any trailing punctuation
        punct = ''
        clean_word = word
        while clean_word and clean_word[-1] in string.punctuation:
            punct = clean_word[-1] + punct
            clean_word = clean_word[:-1]

        if len(clean_word) < 2:
            return word

        # Preserve case pattern
        was_upper = clean_word[0].isupper()
        was_all_upper = clean_word.isupper()
        work_word = clean_word.lower()

        # Choose error type randomly
        error_type = self.rng.choice([
            'substitute', 'delete', 'insert', 'swap', 'double', 'keyboard'
        ])

        if error_type == 'substitute':
            # Replace a vowel with another vowel, or consonant with consonant
            pos = self.rng.randint(0, len(work_word) - 1)
            char = work_word[pos]
            if char in self.VOWELS:
                replacement = self.rng.choice([v for v in self.VOWELS if v != char])
            elif char in self.CONSONANTS:
                replacement = self.rng.choice([c for c in self.CONSONANTS if c != char])
            else:
                replacement = char
            work_word = work_word[:pos] + replacement + work_word[pos+1:]

        elif error_type == 'delete':
            # Delete a random character (not first or last)
            if len(work_word) > 3:
                pos = self.rng.randint(1, len(work_word) - 2)
                work_word = work_word[:pos] + work_word[pos+1:]

        elif error_type == 'insert':
            # Insert a random letter
            pos = self.rng.randint(1, len(work_word) - 1)
            char = self.rng.choice(string.ascii_lowercase)
            work_word = work_word[:pos] + char + work_word[pos:]

        elif error_type == 'swap':
            # Swap two adjacent characters
            if len(work_word) > 2:
                pos = self.rng.randint(0, len(work_word) - 2)
                work_word = (work_word[:pos] + work_word[pos+1] +
                           work_word[pos] + work_word[pos+2:])

        elif error_type == 'double':
            # Double a random letter
            pos = self.rng.randint(0, len(work_word) - 1)
            work_word = work_word[:pos] + work_word[pos] + work_word[pos:]

        elif error_type == 'keyboard':
            # Replace with adjacent keyboard key
            pos = self.rng.randint(0, len(work_word) - 1)
            char = work_word[pos]
            if char in self.KEYBOARD_ADJACENT:
                replacement = self.rng.choice(self.KEYBOARD_ADJACENT[char])
                work_word = work_word[:pos] + replacement + work_word[pos+1:]

        # Restore case
        if was_all_upper:
            work_word = work_word.upper()
        elif was_upper:
            work_word = work_word[0].upper() + work_word[1:]

        return work_word + punct

    def inject_errors(self, text: str, error_rate: float) -> ErrorStats:
        """
        Inject spelling errors into text at the specified rate.

        Args:
            text: The original text
            error_rate: Fraction of words to modify (0.0 to 1.0)

        Returns:
            ErrorStats with original text, modified text, and statistics
        """
        if not 0.0 <= error_rate <= 1.0:
            raise ValueError("error_rate must be between 0.0 and 1.0")

        words = text.split()
        total_words = len(words)

        # Find words eligible for modification
        eligible_indices = [i for i, w in enumerate(words) if self._should_modify_word(w)]

        # Calculate how many words to modify
        num_to_modify = int(len(eligible_indices) * error_rate)

        # Randomly select words to modify
        indices_to_modify = set(self.rng.sample(eligible_indices, min(num_to_modify, len(eligible_indices))))

        # Apply modifications
        modifications = []
        modified_words = []

        for i, word in enumerate(words):
            if i in indices_to_modify:
                modified = self._apply_error(word)
                modifications.append((word, modified))
                modified_words.append(modified)
            else:
                modified_words.append(word)

        modified_text = ' '.join(modified_words)
        actual_rate = len(modifications) / total_words if total_words > 0 else 0.0

        return ErrorStats(
            original_text=text,
            modified_text=modified_text,
            total_words=total_words,
            words_modified=len(modifications),
            actual_error_rate=actual_rate,
            target_error_rate=error_rate,
            modifications=modifications
        )

    def generate_error_variants(self, text: str,
                                error_rates: List[float] = None) -> List[ErrorStats]:
        """
        Generate multiple variants of text with different error rates.

        Args:
            text: The original text
            error_rates: List of error rates to generate (default: 0%, 10%, 20%, 30%, 40%, 50%)

        Returns:
            List of ErrorStats for each error rate
        """
        if error_rates is None:
            error_rates = [0.0, 0.10, 0.20, 0.25, 0.30, 0.40, 0.50]

        variants = []
        for rate in error_rates:
            # Reset RNG for consistency
            self.rng = random.Random(42 + int(rate * 100))
            variants.append(self.inject_errors(text, rate))

        return variants


def main():
    """Demo the spelling error injector."""
    test_sentence = ("The quick brown fox jumps over the lazy dog while the "
                    "beautiful sunset paints the sky with vibrant colors of orange and pink")

    print("=" * 70)
    print("SPELLING ERROR INJECTOR DEMO")
    print("=" * 70)
    print(f"\nOriginal ({len(test_sentence.split())} words):")
    print(f"  {test_sentence}")
    print()

    injector = SpellingErrorInjector(seed=42)

    for rate in [0.0, 0.10, 0.25, 0.30, 0.50]:
        stats = injector.inject_errors(test_sentence, rate)
        print(f"Error Rate: {rate*100:.0f}% (actual: {stats.actual_error_rate*100:.1f}%)")
        print(f"  Words modified: {stats.words_modified}/{stats.total_words}")
        print(f"  Result: {stats.modified_text}")
        if stats.modifications:
            print(f"  Changes: {stats.modifications[:5]}{'...' if len(stats.modifications) > 5 else ''}")
        print()


if __name__ == "__main__":
    main()
