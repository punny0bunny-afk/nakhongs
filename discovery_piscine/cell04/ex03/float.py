num_str = input("Give me a number: ")

try:
    num = float(num_str)
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That is not a valid number.")