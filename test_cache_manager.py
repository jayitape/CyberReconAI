from modules.cache_manager import CacheManager

cache = CacheManager()

cache.set(
    "wordpress",
    {
        "cached": True,
        "cves": [
            "CVE-2022-21661"
        ],
    },
)

print(cache.has("wordpress"))

print(cache.get("wordpress"))

print(cache.size())