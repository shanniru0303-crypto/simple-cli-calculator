# Changelog

## v1.1.0
- Fixed: `divide()` crashed with `ZeroDivisionError` when dividing by zero. Now returns `"Error: Cannot divide by zero"`.
- Fixed: `square_root()` crashed with `ValueError: math domain error` on negative input. Now returns `"Error: Cannot compute square root of a negative number"`.
- Added: `test_cases.py` and `test_runner.py` for automated regression testing.

## v1.0.0
- Initial release: add, subtract, multiply, divide, power, square root via a CLI menu.
