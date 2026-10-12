# pytest output: ============================== 4 passed in 0.01s ===============================
# pylint score: 10.00/10

"""Small functions for the Assignment 0 tools practice."""

from __future__ import annotations


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def mean(nums):
    """Return the arithmetic mean of nums."""
    return sum(nums) / len(nums)


def normalize(nums):
    """Return a new list scaled so it sums to 1.0."""
    total = sum(nums)
    return [num / total for num in nums]


def main() -> None:
    """Entry point for running this file directly."""
    print(greet("Gradescope"))
    print(mean([2, 4, 6]))


if __name__ == "__main__":
    main()
