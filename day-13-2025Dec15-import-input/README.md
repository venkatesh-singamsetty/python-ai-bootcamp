## Python Modules, Input Logic & Bitwise Math

### 📦 1. Imports and Modules

To use tools outside of Python's built-in set, we use the `import` statement.

* **`import numpy as np`**: Loads the NumPy library for array operations. The `as np` part is an **alias** (shorthand) to make coding faster.
* **`import sys`**: Provides access to system-specific parameters and functions, such as command-line arguments.

---

### ⌨️ 2. User Input & the `eval()` Function

Python provides two main ways to capture data from a user:

* **`input()`**: Always treats the entered data as a **string**. If you need a number, you must wrap it: `int(input())`.
* **`eval()`**: The "Smart" converter. It evaluates the input string as a Python expression and automatically assigns the correct data type (e.g., converts `[1,2]` to a **List** or `5` to an **Integer**).

> ⚠️ **Security Warning:** `eval()` is powerful but risky. It will execute any code the user types, so never use it with untrusted or public-facing input.

---

### 🔢 3. Number Systems

Computers don't see "10"; they see electrical states. Python lets you interface with these different bases:

| System | Base | Prefix | Digits/Characters |
| --- | --- | --- | --- |
| **Binary** | 2 | `0b` | 0, 1 |
| **Octal** | 8 | `0o` | 0 - 7 |
| **Decimal** | 10 | *None* | 0 - 9 |
| **Hexadecimal** | 16 | `0x` | 0 - 9, a - f |

**Quick Conversion Functions:**

* `bin(10)`  `'0b1010'`
* `hex(10)`  `'0xa'`
* `oct(10)`  `'0o12'`

---

### ⚡ 4. Bitwise Operators

These operators perform calculations on the **binary bits** of a number rather than the decimal value itself.

* **AND (`&`)**: 1 if both bits are 1.
* **OR (`|`)**: 1 if at least one bit is 1.
* **XOR (`^`)**: 1 if the bits are **different** (one is 1, the other is 0).

---

### ⚖️ 5. Logical vs. Relational Operators

* **Relational (`==`, `>`, `!=`)**: Used to compare two individual values.
* **Logical (`and`, `or`, `not`)**: Used to join multiple relational statements into a single decision.
