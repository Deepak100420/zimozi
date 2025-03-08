import pytest
import sys
import os

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.services.summarization import generate_summary  # Replace with the actual module

def test_generate_summary():
    text = "Artificial intelligence is a branch of computer science that deals with creating intelligent machines."
    summary = generate_summary(text)
    assert isinstance(summary, str)
    assert len(summary) > 10  # Ensure summarization occurs
