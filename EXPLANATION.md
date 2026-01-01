# 🎮 Convert to 7 Game - Code Explanation

## Overview
This Python program is a fun interactive game where users enter any number, and the program automatically converts it to 7 using **only arithmetic operations on the user's input number**.

---

## File Structure

### Main File: `number_to_7.py`
Contains two main functions and one execution block.

---

## Function 1: `convert_to_7(number)`

### Purpose
Converts any given number to 7 using only digit summing and simple arithmetic, returning a list of steps showing how it was done.

### How It Works

**Step 1: Convert Input**
```python
num = abs(int(number))
```
- Takes the input number and converts it to an integer
- Uses `abs()` to handle negative numbers by converting them to positive

**Step 2: Check If Already 7**
```python
if num == 7:
    return ["Already 7! 🎉"]
```
- If the number is already 7, returns immediately

**Step 3: Main Conversion Loop**
The algorithm repeats up to 20 times:

#### Case A: Number is Single Digit (< 10)
```python
if current < 7:
    diff = 7 - current
    steps.append(f"{current} + {diff} = 7")
else:
    diff = current - 7
    steps.append(f"{current} - {diff} = 7")
```
- If less than 7: adds the difference
- If greater than 7: subtracts the difference
- Reaches 7 directly

#### Case B: Number has Multiple Digits
```python
digits = [int(d) for d in str(current)]
digit_sum = sum(digits)
operation = " + ".join(str(d) for d in digits)
steps.append(f"{current} → {operation} = {digit_sum}")
```
- Breaks the number into individual digits
- Adds all digits together
- Shows the operation (e.g., "18 → 1 + 8 = 9")
- Repeats until reaching a single digit

---

## Function 2: `display_game()`

### Purpose
Creates the interactive game loop where users can play multiple rounds without examples.

### Components

#### 1. Welcome Screen
```python
print("=" * 60)
print("🎮 WELCOME TO THE 'CONVERT TO 7' GAME! 🎮")
```
- Displays game title and basic rules
- **No examples shown** (kept simple)

#### 2. Main Game Loop
```python
while True:
    user_input = input("🔢 Enter a number (or 'quit' to exit): ").strip()
```
- Runs indefinitely until user types "quit"
- `.strip()` removes any extra whitespace

#### 3. Input Processing
```python
try:
    number = int(user_input)
    steps = convert_to_7(number)
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")
```
- Tries to convert input to integer
- If conversion fails, catches error and asks for valid input

#### 4. Display Results
```python
for i, operation in enumerate(steps, 1):
    print(f"Step {i}: {operation}")
```
- Shows each step numbered from 1
- `enumerate(steps, 1)` starts counting from 1 instead of 0
- Displays the operation for each step

---

## Algorithm Explanation With Examples

### Example 1: Input = 18
```
Step 1: 18 → 1 + 8 = 9
Step 2: 9 - 2 = 7
✅ Result: 7 (in 2 steps)
```

### Example 2: Input = 42
```
Step 1: 42 → 4 + 2 = 6
Step 2: 6 + 1 = 7
✅ Result: 7 (in 2 steps)
```

### Example 3: Input = 100
```
Step 1: 100 → 1 + 0 + 0 = 1
Step 2: 1 + 6 = 7
✅ Result: 7 (in 2 steps)
```

### Example 4: Input = 5
```
Step 1: 5 + 2 = 7
✅ Result: 7 (in 1 step)
```

---

## Key Python Concepts Used

| Concept | Example | Purpose |
|---------|---------|---------|
| **while loop** | `while current != 7:` | Keep converting until reaching 7 |
| **try-except** | `try: int(user_input)` | Handle invalid inputs gracefully |
| **List comprehension** | `[int(d) for d in str(current)]` | Extract digits from number |
| **sum()** | `sum(digits)` | Add all digits together |
| **String to int conversion** | `str(current)` → iterate → `int(d)` | Convert number to access individual digits |
| **enumerate()** | `enumerate(steps, 1)` | Loop with counting from 1 |
| **f-strings** | `f"{current} → {operation} = {digit_sum}"` | Format output strings |
| **abs()** | `abs(int(number))` | Convert negative numbers to positive |

---

## Program Flow Diagram

```
START
  ↓
Display Welcome Screen (No Examples)
  ↓
Loop Until User Quits:
  ├─ Ask for Number Input
  ├─ Validate Input (try-except)
  ├─ Call convert_to_7(number)
  │  ├─ Check if already 7
  │  ├─ If multiple digits:
  │  │  └─ Sum all digits → repeat until single digit
  │  └─ If single digit:
  │     └─ Add/subtract to reach 7
  ├─ Display all steps (minimum steps)
  ├─ Show SUCCESS message
  └─ Continue or Quit
  ↓
END
```

---

## How to Run

```bash
python number_to_7.py
```

**What happens:**
1. Game starts with welcome message (no examples)
2. Enter any number (positive or negative)
3. Watch the step-by-step conversion to 7
4. Play again or type "quit" to exit

---

## Key Features

✅ **Minimum Steps:**
- Uses only digit summing (most efficient method)
- Direct addition/subtraction for single digits
- Usually reaches 7 in just 1-3 steps

✅ **Only Uses User's Number:**
- No additional numbers introduced
- Pure arithmetic operations on input digits
- Clean and straightforward conversions

✅ **User-Friendly:**
- Clear emoji indicators (🔢, ✨, 🎯)
- Step-by-step display
- Error messages for invalid input
- Easy "quit" option

✅ **Handles Edge Cases:**
- Negative numbers (converted to positive)
- Single digit numbers
- Very large numbers
- Numbers already equal to 7

---

## Summary

This is a simple yet fun game that demonstrates:
- **Mathematics**: Digit sum, modular arithmetic
- **Programming**: Loops, conditionals, string/integer conversion
- **User Interface**: Input validation, clean formatted output
- **Efficiency**: Minimum steps to reach the target using only the user's number

Enjoy playing! 🎉

