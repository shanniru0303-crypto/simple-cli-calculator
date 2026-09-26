# Simple CLI Calculator

A basic command-line calculator written in Python. Supports addition,
subtraction, multiplication, division, power, and square root.

## Usage

```bash
python calculator.py
```

Follow the on-screen menu to pick an operation and enter numbers.

## Running the automated test cases

Test scenarios live in `Calculator_Test_Cases.xlsx`. A corresponding
automated test runner (`test_runner.py`) executes each scenario against
`calculator.py` and prints a pass/fail summary; results are also written
back into the Excel file.

```bash
python test_runner.py
```

## Version History

| Version | Notes |
|---|---|
| 1.0.0 | Initial release: add, subtract, multiply, divide, power, square root. |
| 1.1.0 | Bug fixes: divide-by-zero and negative square-root inputs now return a friendly error message instead of crashing the program. |

## Project Structure

```
calculator.py                  # Calculator application
test_runner.py                 # Automated test runner used to validate test cases
Calculator_Test_Cases.xlsx     # Test scenarios + results
README.md                      # This file
```
