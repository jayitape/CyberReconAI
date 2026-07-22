"""
CyberRecon AI
Concurrent Scan Engine

Version: v1.1.0
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from typing import Any
from typing import Callable

from modules.logger import setup_logger


logger = setup_logger()


class ConcurrentScanner:
    """
    Executes independent scan tasks concurrently.
    """

    def __init__(
        self,
        max_workers: int = 6,
    ) -> None:

        self.max_workers = max_workers

    def run(
        self,
        tasks: dict[str, Callable[[], Any]],
    ) -> dict[str, Any]:
        """
        Execute scan tasks concurrently.

        Args:
            tasks:
                Dictionary containing task name and callable.

        Returns:
            Dictionary containing results.
        """

        results: dict[str, Any] = {}

        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:

            future_map = {
                executor.submit(task): name
                for name, task in tasks.items()
            }

            for future in as_completed(future_map):

                task_name = future_map[future]

                try:

                    results[task_name] = future.result()

                    logger.info(
                        "Concurrent task completed: %s",
                        task_name,
                    )

                except Exception as error:

                    logger.exception(
                        "Concurrent task failed: %s",
                        task_name,
                    )

                    results[task_name] = None

        return results