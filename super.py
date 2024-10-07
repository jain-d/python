#find out the number of times each letter from the alphabets have appeared on in the word.



second_longest_word = "supercalifragilisticexpialidocious"
longest_word = "hippopotomonstrosesquippedaliophobia"
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(f"longest word- {len(longest_word)}")
print(f"second longest word- {len(second_longest_word)}")
for letter in alphabets:
    print(f"{letter} appeared {second_longest_word.count(letter)} times.")
