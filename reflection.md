# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
# When I started the program there were a few issues that the user would run into immediately
  1. The hints are reversed. When you're lower than the number, it is going to tell you to go lower and vice versa
  2. New game doesn't work. It wont refresh anything, and you have to actually restart your page in order for it to refresh.
  3. The difficulty doesn't work. When you pick a difficulty, only the attempts change, not the range of the number
  4. The score is offset by 1, so itll only increment after the 1st round.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


---
# I used Claude code for this project. Initially, when starting this project, I asked Claude to give me a brief breakdown of some of the bugs that exist in this project. A few examples of bugs it gave was the fact that the hints were backwards and the range didnt change no matter what difficulty you chose. I verfied these by not only checking the code to see clear indicators, but also going into the streamlit app and testing it manually. Claude was right in these bugs. However, there were some bugs that were not correct. It said that on even numbered attempts there was an issue with the reliability of hints. However, after fixing the hint direction and checking the game, there seemed to be no issue with the hints, so that was something that was slightly false that I verified.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

# My main way of testing if a bug was fixed was manually going into the game and checking if the specific bug was actually fixed. Since I did one bug at a time, it was easy to go into the game and just reiterate things to make sure it worked. However, I did have Claude help me generate a test for the last bug I solved, which was making the new game button actually refresh the game. I had it focus on just the lines that the bug was fixed in, and then asked it to plan out how best to check if it was fixed or not. It then generated a plan and then code in the test file, after telling me what exactly functional and nonfunctional outputs would look like. The test checks that when a new game is initiated, all the session states are reset. It checks that the status goes from won to playing, to ensure that its properly switching.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
# The secret number kept changing because we kept overriding the number everytime the program did a rerun. Essentially, whenever a Submit Guess was clicked, the random generator reran. Streamlit reruns the entire script whenever something happens on the page, in this case submitting the guess. We use a session state to store specific variables that dont change each rerun. Finally, to fix the problem, instead of refrshing the random number everytime, we put the secret number into the session state so that once the secret is there, it stays there util New game is run and a new session state is generated.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

# In this project, I learned how to iteratively fix bugs with AI, not just say "fix all bugs". I went through each bug myself first, confirmed it with AI, then went one at a time in fixing it. I also committed after every major change, which is a habit I want to built more. After every bug fix, I would check the app, rather than taking AI for its word. I also prompted it to change as minimal lines as possible while still fixing the bug. In this project, I still relied on AI to actually write the fix out for me. In future projects, I want to try to make these fixes on my own, with AI telling me where to surgically do it. Before, i thought of AI generated code as just doing 1000 tasks at once. It would generate everything, things would break, and everything would be generated again. However, in this project, I learned that AI is only as good as the engineer behind it. By prompting correctly, iteratively fixing, and manually testing and checking, AI can be a powerhouse in automatically recognizing and diagnosing bugs, while you're the main architect and checker behind it.
