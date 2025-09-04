# Trying out different string methods in python

word: str = "still wakes the deep"
print(f"\"{word}\"")

# LENGTH of the string in python
print("\nLENGTH")
print(f"\"{word}\" -> \"{len(word)}\"")

# COUNT, gives us count of the number of times a character(s) have appeared
print("\nCOUNT")
print(f"\"{word}\" -> \"{word.count("e")}\"")

# FIND, give us the find index at which we the specified character(s) is found starting from left, -1 if not found
print("\nFIND")
print(f"finding \"e\" in \"{word}\"")
print(word.find("e"))
print("finding \"e\" form the index 10")
print(word.find("e", 10, -2))               #find can take optional arguments for specifying the start and end to the string

# Additionally, rfind gives us the index where the item was found last
print("\nRFIND")
print(f"finding \"e\" from the right side of the string")
print(word.rfind("e"))

# REPLACE, replaces a particular string with another.
print("\nREPLACE")
print(f"replacing \"deep\" with \"dark\" in \"{word}\"")
print(word.replace("deep", "dark"))

# STRIP, removes trailing and preceeding characters(default, whitespace). Doesn't remove the literal string from the beginning/end instead, removes any characters that appear in the specified string 
print("\nSTRIP")
with_spaces = f'-\"{word}\"-'
print(f"striping of \"-\" {with_spaces}")
print(with_spaces.strip("-"))

# Additionally, lstrip and rstrip removes characters from the set(default, whitespace) from the begining and the end.
l_name = " JohnWick"
r_name = "JohnWick--"
print(l_name.lstrip())
print(r_name.rstrip("-"))

# CENTER, centers the string with the given number by adding characters(default, spaces) around it.
print("\nCENTER")
test = "do"
print(f'.{test.center(6, "-")}.')

# RJUST & LJUST, center = rjust + ljust, rjust justifies the string to the right by a certain digit by filling the remaining space with the given character, & vice-versa with ljust
print("\nRJUST")
ac_number_ending = "9309"
print(ac_number_ending.rjust(10, "x"))

# SPLIT, splits the string with the specified character as delimiter and returns as the list
print("\nSPLIT")
print(word.split(" "))
print("split 2")
print(word.split(" ", 2))                       # split can take an optionally parameter for the maximum number of splits we want to peform.
# RSPLIT, split but it work in reverse order, and the significance of the second argument become relevant 
print("rsplit, 2")
print(word.rsplit(" ", 2))                      # starts splitting from the right, and performs atmost 2 splits

# SPLITLINES, splits an entire stream of text based on linebreak as delimiter. So a list, with lines being individual elements
# large_data.splitlines(), for more info, see "../lines.py"

# STARTSWITH, returns boolean for whether a string starts with the particular string, optionally can be extended to include starting and ending indexes too
print("\nSTARTSWITH")
print(f"does \"{word}\" startswith \"still\" -> \"{word.startswith("still")}\"")
print(word.startswith("wa", 6))

# ENDSWITH, does what startswith does, but at the end
print("\nENDSWITH")
print(word.endswith("ep"))
print(word.endswith("the", 12, 15))

# PARTITION, creates a '3 item-tuple' for a string based on the specified string
print("\nPARTITION")
print(word.partition(" "))

# ISALPHA, returns true if all characters of the string are alphabets, whitespace is a  non-alphabetic character 
print("\nISALPHA")
print(f"\"{word}\" isalpha -> \"{word.isalpha()}\"")
print(f"{"".join(word.split(" "))} isalpha -> \"{"".join(word.split(" ")).isalpha()}\"")

# ISNUMERIC, return true if all the characters of the string are numbers
print("\nISNUMERIC")
print(f" \"{word}\" isnumeric -> \"{word.isnumeric()}\"")

# ISALNUM, returns true if the give string is alphanumeric
print("\nISALNUM")
print(f"\"{word}\" is alphanumeric -> \"{word.isalnum()}\"")
print(("3".join(word.split(" "))).isalnum())

# ISSPACE, checks weather a string is whitespace only

# CAPITALIZE, capitalizes the first letter
print("\nCAPITALIZE")
capitalized = word.capitalize()
print(f"\"{word}\" capitalized -> \"{capitalized}\"")

# TITLE, capitalizes the first letter of all the words in the string
print("\nTITLE")
print(word.title())

# CASEFOLD, just like .lower() but more aggressive, meaning would just convert english alphabets to lowercase, will also work with international languages.
print("\nCASEFOLD")
upper = word.upper()
print(upper.casefold())

# SWAPCASE, changes/replaces the case with the other
print("\nSWAPCASE")
print(word.swapcase())

#REMOVEPREFIX, removes a specified substring from the start of a string
print("\nREMOVEPREFIX")
print(f"removing \"il\" using removeprefix")
print(word, "removeprefix ->", word.removeprefix("st"))

#REMOVESUFFIX, just like removeprefix, but instead removes suffix
print("\nREMOVESUFFIX")
print(f"removing \" deep\" using removesuffix")
print(word, "removesuffix ->", word.removesuffix(" deep"))
