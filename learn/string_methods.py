# Trying out different string methods in python

word = "still wakes the deep"
print(f"{word}")

# LENGTH of the string in python
print("\nLENGTH")
print(len(word))

# COUNT, gives us count of the number of times a character(s) have appeared
print("\nCOUNT")
print(word.count("e"))

# FIND, give us the index at which we the specified character(s) is found starting from left, -1 if not found
print("\nFIND")
print(word.find("e"))

# Additionally, rfind gives us the index where the item was found last
print("\nRFIND")
print(word.rfind("e"))

# REPLACE, replaces a particular string with another.
print("\nREPLACE")
print(word.replace("deep", "dark"))

# STRIP, removes trailing and preceeding characters(default, whitespace)
print("\nSTRIP")
with_spaces = f'-{word}-'
print(with_spaces.strip("-"))

# Additionally, lstrip and rstrip removes characters(default, whitespace) from the begining and the end.
l_name = " JohnWick"
r_name = "JohnWick--"
print(l_name.lstrip())
print(r_name.rstrip("-"))

# CENTER, centers the string with the given number by adding characters(default, spaces) around it.
print("\nCENTER")
test = "do"
print(f".{test.center(6, "-")}.")

# RJUST & LJUST, center = rjust + ljust, rjust justifies the string to the right by a certain digit by filling the remaining space with the given character, & vice-versa with ljust
print("\nRJUST")
ac_number_ending = "9309"
print(ac_number_ending.rjust(10, "x"))

# SPLIT, splits the string with the specified character as delimiter and returns as the list
print("\nSPLIT")
print(word.split(" "))

# STARTSWITH, returns boolean for whether a string starts with the particular string, optionally can be extended to include starting and ending indexes too
print("\nSTARTSWITH")
print(word.startswith("still"))
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
print("".join(word.split(" ")).isalpha())

# ISNUMERIC, return true if all the characters of the string are numbers
print("\nISNUMERIC")
print(word.isnumeric())

# ISALNUM, returns true if the give string is alphanumeric
print("\nISALNUM")
print(word.isalnum())
print(("3".join(word.split(" "))).isalnum())

# CAPITALIZE, capitalizes the first letter
print("\nCAPITALIZE")
capitalized = word.capitalize()
print(capitalized)

# CASEFOLD, just like .lower()
print("\nCASEFOLD")
upper = word.upper()
print(upper.casefold())

# SWAPCASE, changes/replaces the case with the other
print("\nSWAPCASE")
print(word.swapcase())
