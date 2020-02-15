from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-param', type=int, choices=[0,1])
    args = parser.parse_args()
    print(args)