import os
import sys

# Make the project root importable so `logic_utils` resolves when pytest
# inserts this test's own directory onto sys.path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess


def test_too_high_guess_tells_player_to_go_lower():
    """Regression: a too-high guess must point the player LOWER.

    The original bug returned 'Go HIGHER!' for a guess above the secret,
    sending the player further from the answer.
    """
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_guess_tells_player_to_go_higher():
    """Regression: a too-low guess must point the player HIGHER."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
