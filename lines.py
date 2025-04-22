with open("./test.txt", "r") as file:
    file_data = file.read()
    lines = file_data.splitlines()
    
print(lines)
