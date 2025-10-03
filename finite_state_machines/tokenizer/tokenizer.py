keywords = {"let", "const", "var" "if", "else", "for", "of", "in", "while", "true", "false", "break", "continue", "switch", "case", "default"}

symbols = {
    "=": "ASSIGNMENT",
    "+": "ADD",
    "-": "SUBTRACT",
    "*": "MULTIPLY",
    "/": "DIVIDE",
    "//": "FDIVIDE",
    "**": "EXPONENT",
    "==": "EQUALS",
    "===": "STRICTEQUALS",
    ";": "SEMICOLON",
    "(": "LPARAN",
    ")": "RPARAN",
    "{": "LCURLY",
    "}": "RCURLY",
    "[": "LSQUARE",
    "]": "RSQUARE"
}

with open("./dummyLanguage.js") as file:
    file_data = file.readlines()

for line in file_data:
    print(line)
