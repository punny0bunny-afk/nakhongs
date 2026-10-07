import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    string_to_search = sys.argv[2]

    matches = re.findall(keyword, string_to_search)
    count = len(matches)

    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()