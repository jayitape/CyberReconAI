"""
CyberRecon AI

Concurrent Scan Engine

Runs independent scan modules simultaneously
to improve scan performance.

Version:
v1.1.0
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


class ConcurrentScanner:
    """
    Execute multiple scan functions concurrently.
    """

    def __init__(self, max_workers: int = 8):
        self.max_workers = max_workers

    def run(self, tasks: dict[str, Callable[[], Any]]) -> dict[str, Any]:
        """
        Execute all tasks concurrently.

        Args:
            tasks:
                Dictionary of task name -> callable.

        Returns:
            Dictionary of results.
        """

        results: dict[str, Any] = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:

            futures = {
                executor.submit(func): name
                for name, func in tasks.items()
            }

            for future in futures:

                name = futures[future]

                try:
                    results[name] = future.result()

                except Exception as error:
                    results[name] = {
                        "error": str(error)
                    }

        return results