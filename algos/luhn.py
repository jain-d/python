""" Luhn's Algorithm

1. from right to left, double value of every second digit, if it is greater then 9, then add the digits 
2. take the sum of all the digits
3. if the sum of all digits is a multiple of 10, then the number is valid

"""
import random

def is_valid_number(number):
    sum = 0
    list_of_number = list(number)
    list_of_number.reverse()
    for value in range(len(list_of_number)):
        current_number = 0
        if value % 2 != 0:
            current_number = int(list_of_number[value]) * 2
            if current_number > 9:
                current_number = (current_number % 10) + (current_number // 10)
        else:
            current_number = int(list_of_number[value])
        sum += current_number
    if (sum % 10 == 0):
        print(number, "is valid")
    else:
        print(number, "is invalid")




inputs = [ "79927398713", "4532015112830366", "6011514433546201", "3222324522261017", "378282246310005",  "1234567890", "9876543210", "6011514433546200", "111111111111111", "1234567891234567" ]
random.shuffle(inputs)

for value in inputs:
    is_valid_number(value)
