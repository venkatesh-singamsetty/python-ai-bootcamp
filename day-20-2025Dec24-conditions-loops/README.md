- PyCharm Debugging (F8 – Step Over)
  - What does F8 do?
   - F8 = Step Over
   - Executes the current line completely and moves to the next line
   - Does not go inside functions


```python
# number is even or odd

x = 4
r = x % 2

if r == 0:
    print("Even")
```

geeksforgeeks.org/conditions-in-python



```python
# nested while

i = 1
while i <= 4:
    j = 0
    while j < 3:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1
```

- `while` -> condition-based looping -> You manage increment manually
- `for` -> sequence-based looping -> manage increment automatically -> List, Tuple, Set, Dictionary, String, Range

# 🔄 Control Flow: Logic, Decision Making & Loops

This section covers how Python makes decisions and repeats tasks, focusing on writing "production-grade" code that is optimized for memory and debugging.

---

## 🚦 Conditional Statements
Conditionals allow the program to branch based on specific criteria.

| Statement | Purpose |
| :--- | :--- |
| **if** | Standard single-condition check. |
| **if-else** | Binary choice (True or False). |
| **if-elif-else** | Multiple mutually exclusive choices. |
| **Nested if** | A condition inside a condition (use for complex logic). |

### 🛑 Professional Insight: The "Multiple If" Warning
In professional organizations, we avoid writing long chains of `if` statements for the same logic. 
* **The Reason:** If you use 10 separate `if` blocks, Python will check **all 10** even if the first one was already true. 
* **Impact:** This wastes CPU memory and slows down execution.
* **The Solution:** Use `elif`. Once one condition is met, Python skips the rest, saving time and resources.

> **💡 Debugging in PyCharm:** When you use the debugger to "step through" code, you will see the marker jump over `elif` blocks once it finds a match. If you use multiple `ifs`, you'll see the marker forced to stop and check every single line—this is what we call "slow memory execution."

---

## 🔁 Loops: Automating Repetition
Loops are used to perform the same action multiple times without rewriting code.



[Image of for loop vs while loop flowcharts]


### 1. While Loop
* **When to use:** When you have a specific **Condition** (e.g., "Keep running as long as the battery is > 20%").
* **Risk:** Always ensure the condition eventually becomes False, or you will create an "Infinite Loop."

### 2. For Loop
* **When to use:** When you have a **Sequence** or a collection (List, Tuple, Set, Dict, String, or Range).
* **Efficiency:** Great for iterating through datasets or cleaning every row in an Excel sheet.

### 🎮 Loop Control Keywords
* **break:** Completely exits the loop immediately.
* **continue:** Skips the current iteration and jumps to the next one in the sequence.
* **pass:** A "do nothing" placeholder. Used when the syntax requires a statement but you aren't ready to write the logic yet.

---

## 📈 Integration with AI & Projects
* **Data Cleaning:** Use `for` loops to iterate through every "Null" value in your IPL dataset.
* **Model Selection:** Use `if-elif` logic to choose which algorithm to run (e.g., `if model == 'KNN': run_knn()`).
* **Debugging:** Use PyCharm breakpoints in your loops to monitor how your variables change at every step of the 5:30 PM Batch project.

---

## 🚀 Final Logic Building Task
Logic building isn't just about syntax; it's about sitting down and mapping out the flow. 
* **Exercise:** Try converting a complex nested `if` into a cleaner `if-elif-else` structure to see how much more readable it becomes.
