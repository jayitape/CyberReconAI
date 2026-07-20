from pprint import pprint
import modules.nvd_client as nvd

print("Loaded from:", nvd.__file__)

client = nvd.NVDClient()

client.cache.clear()   # Force cache clear

vulns = client.search_cves(
    "cpe:2.3:a:wordpress:wordpress:*:*:*:*:*:*:*:*"
)

print(type(vulns))

print(type(vulns[0]))

pprint(vulns[0])