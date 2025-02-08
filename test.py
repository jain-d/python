fileData = open("./test.txt")
fileContent = fileData.read()

print(fileContent.rstrip().split("\n"))

"""
for lines in fileContent:
    print(f"'. {lines}'")
"""
