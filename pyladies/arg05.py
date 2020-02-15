from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('p', nargs='*')
    args = parser.parse_args()
    print(args)