import sys

def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print("none")
        return
        
    text = args[0]
    z_count = 0

    for char in text:
        if char == 'z':
            z_count += 1
            
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)

if __name__ == "__main__":
    main()