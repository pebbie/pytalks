from argparse import ArgumentParser
from glob import glob
if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument('pattern'
, type=str
, nargs='+')
	args = parser.parse_args()
	result = []
	for p in args.pattern:
		result += glob(p)
	for f in result:
		print(f)
