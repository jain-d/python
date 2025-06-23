# Fibonnaci numbers through recursion

def fibonnaci_numbers(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonnaci_numbers(number - 1) + fibonnaci_numbers(number - 2)

inputs = (0, 1, 2, 3, 6, 10)

print("FIBONNACI\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t{fibonnaci_numbers(input)}")
