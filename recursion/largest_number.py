# finding the largest number in an array with recursion
import random
import secrets

def largest_number(array, largest=0):
    if len(array) == 1:
        return array[0]
    potential_largest = largest_number(array[:-1])
    return array[-1] if array[-1] > potential_largest else potential_largest

input = []

for i in range(6):
    input.append(secrets.randbelow(20))

random.shuffle(input)
print(input)
print(largest_number(input))
