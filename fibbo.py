# printing fibonacci series 0 1 1 2 3 5 8

last_value = 0
current_value = 1
print(last_value)
for i in range(9):
    print(current_value)
    current_value += last_value
    last_value = current_value - last_value
