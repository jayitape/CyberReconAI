"""
CyberRecon AI
Enterprise Cache Manager

Provides JSON-based caching for external intelligence
sources such as NVD, EPSS, CISA KEV and ExploitDB.

Version:
v1.1.0
"""

from __future__ import annotations

import json
from pathlib import Path
from threading import Lock
from typing import Any


class CacheManager:
    """
    Generic JSON cache manager.
    """

    def __init__(
        self,
        cache_name: str = "nvd_cache.json",
    ) -> None:
        """
        Initialize cache manager.

        Args:
            cache_name:
                Cache filename.
        """

        self.cache_dir = Path("cache")
        self.cache_dir.mkdir(
            exist_ok=True
        )

        self.cache_file = self.cache_dir / cache_name

        self._lock = Lock()

        self._cache: dict[str, Any] = {}

        self._load()

    def _load(self) -> None:
        """
        Load cache from disk.
        """

        if not self.cache_file.exists():

            self._cache = {}

            self._save()

            return

        try:

            with self.cache_file.open(
                "r",
                encoding="utf-8",
            ) as file:

                self._cache = json.load(file)

        except (
            json.JSONDecodeError,
            OSError,
        ):

            self._cache = {}

            self._save()

    def _save(self) -> None:
        """
        Save cache to disk.
        """

        with self._lock:

            with self.cache_file.open(
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    self._cache,
                    file,
                    indent=4,
                    ensure_ascii=False,
                )

    def has(
        self,
        key: str,
    ) -> bool:
        """
        Check if cache contains key.
        """

        return key in self._cache

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Get cached value.
        """

        return self._cache.get(
            key,
            default,
        )

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store cache value.
        """

        self._cache[key] = value

        self._save()

    def remove(
        self,
        key: str,
    ) -> None:
        """
        Remove cached value.
        """

        if key in self._cache:

            del self._cache[key]

            self._save()

    def clear(self) -> None:
        """
        Clear entire cache.
        """

        self._cache.clear()

        self._save()

    def keys(
        self,
    ) -> list[str]:
        """
        Return cached keys.
        """

        return list(
            self._cache.keys()
        )

    def size(
        self,
    ) -> int:
        """
        Return number of cached entries.
        """

        return len(
            self._cache
        )