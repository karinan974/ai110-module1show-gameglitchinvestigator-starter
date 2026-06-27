# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**
  It's a Streamlit number-guessing game. The app picks a secret number in a
  range that depends on the chosen difficulty (Easy/Normal/Hard). The player
  types a guess and gets a hint — "Too High" or "Too Low" — until they land on
  the secret. A score updates with each attempt, and the game ends on a win or
  when attempts run out.

- [x] **Detail which bugs you found.**
  - **Backwards hints (logic bug):** a guess *above* the secret returned
    "📈 Go HIGHER!" and a guess *below* returned "📉 Go LOWER!", pushing the
    player away from the answer.
  - **Fragile secret comparison:** on even-numbered attempts the app passes the
    secret as a string, which made `check_guess` fall back to comparing text
    instead of numbers (e.g. `"9" > "30"` is `True`), giving wrong hints.
  - **Game logic in the wrong file:** `check_guess` and `parse_guess` lived in
    `app.py` instead of `logic_utils.py`, so they couldn't be tested cleanly.

- [x] **Explain what fixes you applied.**
  - Swapped the hint messages so a too-high guess now says "Go LOWER!" and a
    too-low guess says "Go HIGHER!".
  - Added `int(guess)`/`int(secret)` coercion in `check_guess` so number vs.
    string never breaks the comparison.
  - Moved `check_guess` and `parse_guess` into `logic_utils.py` and imported
    them back into `app.py`.
  - Added a pytest regression test covering both hint directions.

## 📸 Demo Walkthrough

1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of 70 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

# ====================================================== test session starts ======================================================
# platform darwin -- Python 3.9.0, pytest-8.4.2, pluggy-1.6.0 -- /Users/karinanaranjo/ai110-module1show-gameglitchinvestigator-starter/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/karinanaranjo/ai110-module1show-gameglitchinvestigator-starter
# collected 2 items                                                                                                               

# test/test_game_logic.py::test_too_high_guess_tells_player_to_go_lower PASSED                                              [ 50%]
# test/test_game_logic.py::test_too_low_guess_tells_player_to_go_higher PASSED                                              [100%]

# ======================================================= 2 passed in 0.01s =======================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
