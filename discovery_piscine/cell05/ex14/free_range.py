import sys

if len(sys.argv)!= 3:
    print("none")

else:
    start = int(sys.argv[1])

    end = int(sys.argv[2])

    numbers = list(range(start,end))

    print(numbers)