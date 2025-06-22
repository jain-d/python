# Classic recursion problem, the factorial of a number

def calculate_factorial(number):
    if number == 0:
        return 1
    return number * calculate_factorial(number - 1)

inputs = (5, 0, 3)

print("FACTORIAL\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t{calculate_factorial(input)}")
