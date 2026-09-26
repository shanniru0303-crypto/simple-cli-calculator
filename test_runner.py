"""
Test runner for the Simple CLI Calculator.

Executes every scenario in test_cases.py directly against the functions
in calculator.py, then prints (and can export) Pass/Fail results.
"""

import json
import sys

import calculator
from test_cases import TEST_CASES


def is_close(a, b, tol=1e-6):
    try:
        return abs(float(a) - float(b)) < tol
    except (TypeError, ValueError):
        return False


def run_tests():
    results = []
    func_map = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
        "power": calculator.power,
        "square_root": calculator.square_root,
    }

    for tc in TEST_CASES:
        func = func_map[tc["function"]]
        inputs = tc["inputs"]

        try:
            result = func(*inputs)
            crashed = False
            error_text = None
        except Exception as e:  # noqa: BLE001 - we want to catch any crash
            result = None
            crashed = True
            error_text = f"{type(e).__name__}: {e}"

        if crashed:
            actual = f"CRASHED - {error_text}"
            status = "FAIL"
        elif tc["check"] == "value":
            actual = str(result)
            status = "PASS" if is_close(result, tc["expected_value"]) else "FAIL"
        elif tc["check"] == "graceful_error":
            # Passes only if the function returned a string containing
            # "Error" instead of raising / crashing.
            actual = str(result)
            status = "PASS" if isinstance(result, str) and "Error" in result else "FAIL"
        else:
            actual = str(result)
            status = "FAIL"

        results.append(
            {
                "id": tc["id"],
                "scenario": tc["scenario"],
                "steps": tc["steps"],
                "expected": tc["expected"],
                "actual": actual,
                "status": status,
            }
        )

    return results


def main():
    results = run_tests()
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed

    for r in results:
        print(f"[{r['status']}] {r['id']} - {r['scenario']}")
        print(f"        Expected: {r['expected']}")
        print(f"        Actual  : {r['actual']}")

    print("\n---------------------------------------------")
    print(f"Version under test: {calculator.VERSION}")
    print(f"Total: {len(results)}  Passed: {passed}  Failed: {failed}")
    print("---------------------------------------------")

    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        with open("results.json", "w") as f:
            json.dump(
                {"version": calculator.VERSION, "results": results}, f, indent=2
            )
        print("Results written to results.json")

    return failed


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
