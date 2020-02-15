from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser(
        description="hi", epilog="bye"
    )
    args = parser.parse_args()
