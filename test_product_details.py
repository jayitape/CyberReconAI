from modules.cpe_mapper import CPEMapper


def main() -> None:

    mapper = CPEMapper()

    result = mapper.get_product_details(
        "wordpress"
    )

    print(result)


if __name__ == "__main__":
    main()