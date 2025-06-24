# finding the number of letter occurances in a word with recursion

def count_occurance(word, letter):
    if not len(word):
        return 0
    return int(word[-1] == letter) + count_occurance(word[:-1], letter)

inputs = [("hello", "l"), ("recursion", "r"), ("python", "z"), ("", "a"), ("pulp fiction", "")]

print("RECUSION\n\nINPUT\tVALUE")
for input in inputs:
    print(f"{input}\t{count_occurance(*input)}")
