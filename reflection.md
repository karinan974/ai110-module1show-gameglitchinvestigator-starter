# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  " "  | Null              |        0        |  No Output / Error     |
|  25   | Go Lower          |  Go Higher      |    Go HIGHER!          |
|  5    | Go Higher         |  Go Lower       |    Go LOWER!           |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The way I prompted the AI to assist with the "Too High / Too Low Error":

I have a bug in my code scan through this files to help me find and fix the bug @app.py  @logic_utils.py . How it is supposed to work (logic): When the guess is higher than the secret number it's should to print "Too High", "📈 Go LOWER!" and when the guess is lower than the secret number it's should  to print "Too Low", "📉 Go HIGHER". The current logic does not do this. I did put this comment,  # FIXME: Logic breaks here; where I believe the issue is. 

This provided both correct and incorrect. 
Correct: It was correctly fixing the logic within app.py 
Incorrect: Although the logic was being fixed it was not taking into consideration logic_utils.py to transfer the game logic to that file.

To verify the code I ran app.py with the fixes and played the game to make 
sure the output was accurate. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# I decided a bug is really fixed when the logic is functioning as expected and it passes the py test as that asserts the functions and logic is working as expected (verification)
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
# Manually I played the game to test that as I inputted guesses it would output the expected result such as Go Higher or Lower and using pytest I was also testing this.
- Did AI help you design or understand any tests? How?
# Yes AI helped me design and understand the tests. I prompted the AI with the types of pytest I wanted to generate and then asked it to explain how the test worked both in technical language and elementry school (using examples).

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
# When you run Streamlit it runs your python script from top to bottom. Replays the movie from the beginning.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
# Before starting the lab; read each file and understand what each file does. This will help me better prompt and understand if the AI is directing me the correct way.
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
# Provide it more context.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# AI generated code can be super helpful and facilitate things, but it can also give you shortcuts if not promoted correctly and shortcuts does not mean it is correct.
