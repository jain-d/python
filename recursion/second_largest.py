# Second largest number using recursion
import random

def second_largest(array):
    if len(array) == 2:
        array.sort()
        return array

    biggest_two = second_largest(array[1:])
    if array[0] > biggest_two[1]:
        biggest_two.pop(0)
        biggest_two.append(array[0])
    elif array[0] > biggest_two[0]:
        biggest_two.pop(0)
        biggest_two.insert(0, array[0])
    return biggest_two
    
    

inputs = [[1, 2, 3, 4, 5], [7, 8, 1, 2]]

for _ in range(5):
    inputs.append([random.randrange(29) for _ in range(5)])

print("\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t\t{second_largest(input)}")
