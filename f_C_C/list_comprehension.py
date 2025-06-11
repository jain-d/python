camel_or_pascal = ["aComplexAndLongString", "CSharpIsJustBad"]

snake_cased = [("".join([char if char.islower() else ("_" + char.lower()) for char in entry])).strip("_") for entry in camel_or_pascal]

print(snake_cased)
