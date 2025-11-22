#!/usr/bin/env python3
"""
Pytest configuration and shared fixtures.

This file is automatically loaded by pytest and provides shared fixtures
and configuration for all test files in the tests directory.
"""

import sys
import os

# Add scripts directory to path for imports
scripts_dir = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, scripts_dir)


def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to handle slow tests."""
    # If running in CI or with --quick flag, skip slow tests by default
    if config.getoption("-m"):
        # User specified markers, respect their choice
        return

    # Add skip marker to slow tests if not explicitly requested
    skip_slow = pytest.mark.skip(reason="Skipping slow test (use -m slow to run)")

    for item in items:
        if "slow" in item.keywords:
            # Only skip if user didn't explicitly request slow tests
            pass  # Let them run by default


# Import pytest here to use in pytest_collection_modifyitems
import pytest


@pytest.fixture(scope="session")
def project_root():
    """Return the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="session")
def scripts_dir(project_root):
    """Return the scripts directory."""
    return os.path.join(project_root, 'scripts')


@pytest.fixture(scope="session")
def agents_dir(project_root):
    """Return the agents directory."""
    return os.path.join(project_root, 'agents')


@pytest.fixture(scope="session")
def skills_dir(project_root):
    """Return the skills directory."""
    return os.path.join(project_root, 'skills')


@pytest.fixture
def sample_english_sentence():
    """Provide a sample English sentence with 15+ words."""
    return ("The magnificent golden sunset painted the entire western sky "
            "with beautiful shades of orange, pink, and deep purple colors.")


@pytest.fixture
def sample_misspelled_sentence():
    """Provide a misspelled version of the sample sentence (~25% errors)."""
    return ("The magnificant goldon sunset paintd the entier western skye "
            "with beautful shades of oraneg, pink, and deap purpel colors.")
