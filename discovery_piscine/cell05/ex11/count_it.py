import sys

def main():
    args = sys.argv[1:]
    
    if not args:
        print("none")
    else:
        print(f"parameters: {len(args)}")
        for arg in args:
            print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    main()