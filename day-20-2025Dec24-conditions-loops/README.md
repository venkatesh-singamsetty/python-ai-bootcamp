## Control Flow & Debugging: Study Notes

### 🐞 PyCharm Debugging: Mastering Execution

Debugging is the process of pausing your code to inspect its "health" mid-run.

* **F8 (Step Over):** The most common debugging command.
* **Action:** Executes the current line completely and moves to the next line.
* **Behavior:** It **does not** enter into functions. If the line calls a function, it runs it in the background and simply gives you the result on the next line.


* **Why Debug?** It allows you to monitor how variables (like `i` or `r`) change in real-time, helping you catch logic errors before they crash your program.

---

### 🚦 Decision Making: Conditional Logic

Python uses indented blocks to determine which code to execute based on truth values.

#### **Core Syntax**

```python
# Even or Odd Example
x = 4
r = x % 2  # Modulus returns the remainder

if r == 0:
    print("Even")
else:
    print("Odd")

```

#### **Efficiency Tip: `if` vs. `elif**`

* **Multiple `if` statements:** Python evaluates **every single block**, even if the first one was True. This consumes more CPU and memory.
* **`elif` (Else If):** Python stops checking as soon as it finds a True condition. This is **"Production-Grade"** code because it optimizes execution speed.

---

### 🔁 Looping: For vs. While

Loops automate repetitive tasks, but they handle "counting" differently.

| Feature | `while` Loop | `for` Loop |
| --- | --- | --- |
| **Primary Use** | **Condition-based** logic. | **Sequence-based** iteration. |
| **Control** | You must manually increment/update the counter. | Python manages the increment/traversal automatically. |
| **Targets** | Thresholds (e.g., `while battery > 10%`). | Collections (List, Tuple, Set, Dict, Range, String). |

#### **Nested Loops (Matrix/Grid Logic)**

When you put a loop inside another, the inner loop completes all its iterations for every **single** step of the outer loop.

```python
# Nested While Example
i = 1
while i <= 4:      # Outer loop
    j = 0
    while j < 3:   # Inner loop
        print(i * j, end=" ")
        j += 1
    print()        # New line after inner loop finishes
    i += 1

```

---

### 🎮 Loop Control Keywords

* **`break`**: The "Emergency Exit." Immediately kills the loop.
* **`continue`**: The "Skip Button." Jumps to the start of the next iteration, skipping the code below it.
* **`pass`**: The "Empty Placeholder." Used when syntax requires a line of code, but you aren't ready to write the logic yet (prevents errors).

---

### 💡 Application in the IPL Project

* **`for` loop:** Use this to scan through every row of your IPL dataset to find specific match trends.
* **`if-elif`**: Use this to categorize teams based on their win percentage (e.g., `> 80%` = "Elite", `> 50%` = "Competitive").
