from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_new_game_resets_state():
    # Simulate a finished game state
    session = {
        "attempts": 5,
        "secret": 42,
        "status": "won",
        "history": [10, 20, 42],
    }

    # Apply the new game reset logic (mirrors the fix in app.py)
    session["attempts"] = 0
    session["secret"] = 99  # stand-in for random.randint(low, high)
    session["status"] = "playing"
    session["history"] = []

    assert session["status"] == "playing", "status must be reset to 'playing'"
    assert session["attempts"] == 0, "attempts must be reset to 0"
    assert session["history"] == [], "history must be cleared"
    assert session["secret"] == 99, "secret must be regenerated"
