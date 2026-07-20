from modules.nvd_client import NVDClient
from modules.cve_parser import CVEParser


def main() -> None:

    client = NVDClient()

    records = client.search_cves(
        "cpe:2.3:a:wordpress:wordpress:*:*:*:*:*:*:*:*"
    )

    parser = CVEParser()

    result = parser.parse_multiple(
        records[:3]
    )

    for item in result:
        print(item)


if __name__ == "__main__":
    main()