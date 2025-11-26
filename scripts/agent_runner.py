#!/usr/bin/env python3
"""
Agent Runner - CLI interface for running translation agents via Claude API.

This script provides a programmatic way to run the translation agents
defined in the .claude/commands directory using the Anthropic API.

Usage:
    python agent_runner.py --agent en-fr --text "Your text here"
    python agent_runner.py --agent fr-he --text "Votre texte ici"
    python agent_runner.py --agent he-en --text "הטקסט שלך כאן"
    python agent_runner.py --agent roundtrip --text "Your text here"
    python agent_runner.py --pipeline --text "Your text here"  # Full pipeline
"""

import os
import sys
import argparse
from typing import Optional, Dict, Tuple
from dataclasses import dataclass

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed.")
    print("Install with: pip install anthropic")
    sys.exit(1)


@dataclass
class AgentConfig:
    """Configuration for a translation agent."""
    name: str
    description: str
    source_lang: str
    target_lang: str
    system_prompt: str


# Agent configurations based on the .claude/commands and agents/ definitions
AGENTS = {
    "en-fr": AgentConfig(
        name="English to French Translator",
        description="Agent 1: Translates English to French",
        source_lang="English",
        target_lang="French",
        system_prompt="""You are an expert English to French translator. Follow these guidelines:

1. **Subjunctive Mood**: Use subjunctive for doubt, emotion, desire, necessity
   - "I want him to come" → "Je veux qu'il vienne"

2. **Partitive Articles**: Use du/de la/de l'/des appropriately
   - "I eat bread" → "Je mange du pain"

3. **Subject Pronouns**: Always include (je, tu, il, elle, etc.)

4. **Word Order**: BANGS adjectives before nouns, others after
   - "a red car" → "une voiture rouge"

5. **Natural Phrasing**: Avoid literal translations
   - "I miss you" → "Tu me manques"
   - "I am cold" → "J'ai froid"
   - "I am 20 years old" → "J'ai 20 ans"

Handle spelling errors in input by understanding intended meaning.
Return ONLY the French translation with no explanations."""
    ),

    "fr-he": AgentConfig(
        name="French to Hebrew Translator",
        description="Agent 2: Translates French to Hebrew",
        source_lang="French",
        target_lang="Hebrew",
        system_prompt="""You are an expert French to Hebrew translator. Follow these guidelines:

1. **Gender Independence**: French gender does NOT transfer to Hebrew
   - Look up Hebrew gender independently for each noun
   - "la plage" (feminine French) → "החוף" (masculine Hebrew)

2. **Binyan Selection**: Choose correct Hebrew verb pattern:
   - Pa'al for simple actions (לכתוב)
   - Nif'al for passive/reflexive (להיכתב)
   - Pi'el for intensive (לכתֵּב)
   - Hif'il for causative (להכתיב)
   - Hitpa'el for reflexive (להתכתב)

3. **Article Conversion**:
   - French le/la/les → Hebrew ה prefix
   - French un/une → No Hebrew equivalent

4. **Tense Mapping**:
   - passé composé → Hebrew past
   - futur → Hebrew future
   - subjonctif → Hebrew future (usually)

Return ONLY the Hebrew translation with no explanations."""
    ),

    "he-en": AgentConfig(
        name="Hebrew to English Translator",
        description="Agent 3: Translates Hebrew to English",
        source_lang="Hebrew",
        target_lang="English",
        system_prompt="""You are an expert Hebrew to English translator. Follow these guidelines:

1. **Nikud Resolution**: Resolve vowel ambiguities using context
   - כתב could be "wrote", "writing", "writes" - use context

2. **Binyan Mapping**: Map Hebrew verb patterns to English verbs appropriately

3. **Word Order Transformation**: Convert VSO to SVO
   - "הלך הילד לבית" → "The child went home" (not "Went the child home")

4. **Gender-to-Pronoun Mapping**:
   - Feminine -ת ending → use "she"
   - Masculine form → use "he"

5. **Prefix Expansion**:
   - ב → "in"
   - ל → "to"
   - מ → "from"
   - ה → "the"

Make the output sound like natural, native English.
Return ONLY the English translation with no explanations."""
    ),
}


class TranslationAgent:
    """Wrapper for running translation agents via Claude API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-20250514"):
        """
        Initialize the translation agent.

        Args:
            api_key: Anthropic API key (uses env var if not provided)
            model: Claude model to use
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model

    def translate(self, text: str, agent_id: str) -> str:
        """
        Translate text using the specified agent.

        Args:
            text: Text to translate
            agent_id: Agent identifier ("en-fr", "fr-he", or "he-en")

        Returns:
            Translated text
        """
        if agent_id not in AGENTS:
            raise ValueError(f"Unknown agent: {agent_id}. Valid: {list(AGENTS.keys())}")

        agent = AGENTS[agent_id]

        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=agent.system_prompt,
            messages=[
                {"role": "user", "content": f"Translate this {agent.source_lang} text to {agent.target_lang}:\n\n{text}"}
            ]
        )

        return message.content[0].text.strip()

    def run_pipeline(self, text: str, verbose: bool = True) -> Tuple[str, str, str]:
        """
        Run the full translation pipeline: EN → FR → HE → EN

        Args:
            text: English text to translate
            verbose: Print progress

        Returns:
            Tuple of (french, hebrew, final_english)
        """
        if verbose:
            print("\n" + "=" * 60)
            print("TRANSLATION PIPELINE")
            print("=" * 60)
            print(f"\nOriginal: {text}")

        # Step 1: English → French
        if verbose:
            print("\n--- Step 1: English → French ---")
        french = self.translate(text, "en-fr")
        if verbose:
            print(f"French: {french}")

        # Step 2: French → Hebrew
        if verbose:
            print("\n--- Step 2: French → Hebrew ---")
        hebrew = self.translate(french, "fr-he")
        if verbose:
            print(f"Hebrew: {hebrew}")

        # Step 3: Hebrew → English
        if verbose:
            print("\n--- Step 3: Hebrew → English ---")
        final_english = self.translate(hebrew, "he-en")
        if verbose:
            print(f"Final English: {final_english}")
            print("\n" + "=" * 60)

        return french, hebrew, final_english


def main():
    parser = argparse.ArgumentParser(
        description="Run translation agents via Claude API"
    )
    parser.add_argument('--agent', type=str, choices=list(AGENTS.keys()),
                       help='Agent to use for translation')
    parser.add_argument('--pipeline', action='store_true',
                       help='Run full translation pipeline (EN → FR → HE → EN)')
    parser.add_argument('--text', type=str, required=True,
                       help='Text to translate')
    parser.add_argument('--api-key', type=str,
                       help='Anthropic API key (or use ANTHROPIC_API_KEY env var)')
    parser.add_argument('--model', type=str, default='claude-sonnet-4-20250514',
                       help='Claude model to use')
    parser.add_argument('--quiet', action='store_true',
                       help='Suppress verbose output')

    args = parser.parse_args()

    if not args.agent and not args.pipeline:
        parser.error("Either --agent or --pipeline must be specified")

    try:
        agent = TranslationAgent(api_key=args.api_key, model=args.model)

        if args.pipeline:
            french, hebrew, final = agent.run_pipeline(args.text, verbose=not args.quiet)
            if args.quiet:
                print(final)
        else:
            result = agent.translate(args.text, args.agent)
            print(result)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"API Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
