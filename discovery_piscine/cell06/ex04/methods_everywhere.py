import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

def main():
    args = sys.argv[1:]
 
    if len(args) < 1:
        print("none")
        return

    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()