#!/usr/bin/env python3
"""
Local Translation Agents - Real translations without API

Uses Helsinki-NLP MarianMT models for offline translation.
No API key required - models run locally on your machine.

Models used:
- English → French: Helsinki-NLP/opus-mt-en-fr
- French → Hebrew: Helsinki-NLP/opus-mt-fr-he
- Hebrew → English: Helsinki-NLP/opus-mt-he-en

First run downloads models (~300MB each). Subsequent runs are fast.

Usage:
    python local_translation_agents.py --text "Your text here"
    python local_translation_agents.py --agent en-fr --text "Hello world"
    python local_translation_agents.py --pipeline --text "Your text here"
"""

import os
import sys
import argparse
from typing import Tuple, Optional
from dataclasses import dataclass

try:
    from transformers import MarianMTModel, MarianTokenizer
except ImportError:
    print("Error: transformers package not installed.")
    print("Install with: python -m pip install transformers sentencepiece")
    sys.exit(1)


@dataclass
class TranslationAgent:
    """A local translation agent using MarianMT."""
    name: str
    model_name: str
    source_lang: str
    target_lang: str
    model: Optional[MarianMTModel] = None
    tokenizer: Optional[MarianTokenizer] = None


class LocalTranslationPipeline:
    """Pipeline of local translation agents."""

    # Model mappings for each translation direction
    # Note: he-en uses afa-en (afroasiatic family includes Hebrew)
    MODELS = {
        "en-fr": "Helsinki-NLP/opus-mt-en-fr",
        "fr-he": "Helsinki-NLP/opus-mt-fr-he",
        "he-en": "Helsinki-NLP/opus-mt-afa-en",  # afa = afroasiatic (includes Hebrew)
    }

    def __init__(self, verbose: bool = True):
        """
        Initialize the local translation pipeline.

        Args:
            verbose: Print progress messages
        """
        self.verbose = verbose
        self.agents = {}

    def _log(self, message: str):
        """Print message if verbose mode is on."""
        if self.verbose:
            print(message)

    def load_agent(self, agent_id: str) -> TranslationAgent:
        """
        Load a translation agent (downloads model if needed).

        Args:
            agent_id: Agent identifier ("en-fr", "fr-he", or "he-en")

        Returns:
            Loaded TranslationAgent
        """
        if agent_id in self.agents:
            return self.agents[agent_id]

        if agent_id not in self.MODELS:
            raise ValueError(f"Unknown agent: {agent_id}. Valid: {list(self.MODELS.keys())}")

        model_name = self.MODELS[agent_id]
        source, target = agent_id.split("-")

        lang_names = {"en": "English", "fr": "French", "he": "Hebrew"}

        self._log(f"Loading {lang_names[source]} -> {lang_names[target]} agent...")
        self._log(f"  Model: {model_name}")
        self._log(f"  (First run downloads ~300MB, please wait...)")

        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

        agent = TranslationAgent(
            name=f"{lang_names[source]} to {lang_names[target]}",
            model_name=model_name,
            source_lang=lang_names[source],
            target_lang=lang_names[target],
            model=model,
            tokenizer=tokenizer
        )

        self.agents[agent_id] = agent
        self._log(f"  Agent loaded successfully!")

        return agent

    def translate(self, text: str, agent_id: str) -> str:
        """
        Translate text using specified agent.

        Args:
            text: Text to translate
            agent_id: Agent identifier ("en-fr", "fr-he", or "he-en")

        Returns:
            Translated text
        """
        agent = self.load_agent(agent_id)

        # Tokenize
        inputs = agent.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

        # Generate translation
        translated = agent.model.generate(**inputs)

        # Decode
        result = agent.tokenizer.decode(translated[0], skip_special_tokens=True)

        return result

    def run_pipeline(self, text: str) -> Tuple[str, str, str]:
        """
        Run full translation pipeline: EN -> FR -> HE -> EN

        Args:
            text: English text to translate

        Returns:
            Tuple of (french, hebrew, final_english)
        """
        self._log("\n" + "=" * 60)
        self._log("LOCAL TRANSLATION PIPELINE (No API)")
        self._log("=" * 60)
        self._log(f"\nOriginal: {text}")

        # Step 1: English -> French
        self._log("\n--- Step 1: English -> French ---")
        french = self.translate(text, "en-fr")
        self._log(f"French: {french}")

        # Step 2: French -> Hebrew
        self._log("\n--- Step 2: French -> Hebrew ---")
        hebrew = self.translate(french, "fr-he")
        self._log(f"Hebrew: {hebrew}")

        # Step 3: Hebrew -> English
        self._log("\n--- Step 3: Hebrew -> English ---")
        final_english = self.translate(hebrew, "he-en")
        self._log(f"Final English: {final_english}")

        self._log("\n" + "=" * 60)

        return french, hebrew, final_english


def main():
    parser = argparse.ArgumentParser(
        description="Local translation agents using MarianMT (no API required)"
    )
    parser.add_argument('--agent', type=str, choices=['en-fr', 'fr-he', 'he-en'],
                       help='Single agent to use')
    parser.add_argument('--pipeline', action='store_true',
                       help='Run full pipeline (EN -> FR -> HE -> EN)')
    parser.add_argument('--text', type=str, required=True,
                       help='Text to translate')
    parser.add_argument('--quiet', action='store_true',
                       help='Suppress verbose output')

    args = parser.parse_args()

    if not args.agent and not args.pipeline:
        # Default to pipeline
        args.pipeline = True

    pipeline = LocalTranslationPipeline(verbose=not args.quiet)

    if args.pipeline:
        french, hebrew, final = pipeline.run_pipeline(args.text)
        if args.quiet:
            print(f"French: {french}")
            print(f"Hebrew: {hebrew}")
            print(f"English: {final}")
    else:
        result = pipeline.translate(args.text, args.agent)
        print(result)


if __name__ == "__main__":
    main()
