from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('p', type=int)
    args = parser.parse_args()
    print(args)