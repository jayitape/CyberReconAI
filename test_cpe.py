from modules.cpe_mapper import CPEMapper


def main() -> None:
    mapper = CPEMapper()

    result = mapper.map_technologies(
        [
            "nginx",
            "wordpress",
            "unknown",
        ]
    )

    print(result)


if __name__ == "__main__":
    main()