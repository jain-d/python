# calculate the sum of digits in a positive integer, through recursion
# input 123, output 5

def sum_of_digits(positive_integer):
    if positive_integer > 0:
        return positive_integer % 10 + sum_of_digits(int(positive_integer / 10))
    else:
        return 0

inputs = (123, 45, 7, 0)

for input in inputs:
    print(f"{input}. {sum_of_digits(input)}")
