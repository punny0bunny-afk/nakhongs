import sys

if len(sys.argv) == 2:
    user_word = input("What was the parameter? ")
    if user_word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")