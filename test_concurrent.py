"""
CyberRecon AI
Concurrent Scanner Test

Version: v1.0.20
"""

from time import sleep

from modules.concurrent_scanner import ConcurrentScanner


def task_one() -> str:
    """
    Simulate first concurrent task.

    Returns:
        str: Task result.
    """
    sleep(2)
    return "Done 1"


def task_two() -> str:
    """
    Simulate second concurrent task.

    Returns:
        str: Task result.
    """
    sleep(1)
    return "Done 2"


def task_three() -> str:
    """
    Simulate third concurrent task.

    Returns:
        str: Task result.
    """
    sleep(3)
    return "Done 3"


def main() -> None:
    """
    Run concurrent scanner test.
    """
    scanner = ConcurrentScanner()

    tasks = {
        "one": task_one,
        "two": task_two,
        "three": task_three,
    }

    results = scanner.run(tasks)

    print("\nConcurrent Scanner Results")
    print("-" * 40)

    for name, result in results.items():
        print(f"{name:<10} : {result}")


if __name__ == "__main__":
    main()