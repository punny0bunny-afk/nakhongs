import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for arg in reversed(args):
        print(arg)