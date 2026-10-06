num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))

result = num1 * num2
if num1.is_integer(): num1 = int(num1)
if num2.is_integer(): num2 = int(num2)
if result.is_integer(): result = int(result)

print(f"{num1} x {num2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")