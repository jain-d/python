# Fibonnaci numbers through recursion

def fibonnaci_numbers(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonnaci_numbers(number - 1) + fibonnaci_numbers(number - 2)

def old_way(number):  
    previous_number = 0
    fib_number = 0
    for index in range(number + 1):
        if index == 1:
            fib_number += 1
        else:
            fib_number += previous_number
            previous_number = fib_number - previous_number
    return fib_number

inputs = (0, 1, 2, 3, 6, 10)

print("FIBONNACI\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t{fibonnaci_numbers(input)}")


print("OLD FIBONNACI\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t{old_way(input)}")
