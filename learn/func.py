# Normal function
def say_hello():
    print("this dumb function just says hello")
    print("\n")

say_hello()


# Parameterized function
def greet(greeting):
    print(f"this function says '{greeting}', obtained through a parameter.")
    print("\n")

greet("SayoNara")


# function with Positional Parameters
def positional_parameters(first, second):
    print(f"this the first parameter = '{first}', and this is the second one = '{second}'")
    print("\n")

positional_parameters("hello", "world")


# function with Arbitrary Arguments
def arbitrary_arguments(*all):
    print("this function takes arbitrary number of arguments, they are the following =")
    for value in all:
        print(value)
    print("\n")

arbitrary_arguments("one", 2, "three", 4.3, False, ["x", "y", "z"])


# function with Keyword arguments
def keyword_arguments(first, second):
    print(f"this function has parameters that are keyword based")
    print(f"first = {first}, second = {second}")
    print("\n")

keyword_arguments(second="don", first="quixote")


# function with Arbitrary Keyword Arguments
def arbitrary_keyword_arguments(**everything):
    print("this function catches arbitrary number of keyword argument as a dictionary")
    for key in everything:
        print(f"{key}: {everything[key]}")
    print("\n")

arbitrary_keyword_arguments(name="John Wick", age=40, city="New York")


# Positional-Only Arguments
def positional_only(pos_one, pos_two, /):
    print("this function only takes in positional arguments, no keyword arguments allowed")
    print(f"{pos_one}, {pos_two}")
    print("\n")

positional_only("with love", "from python")


# Keyword-Only Arguments
def keyword_only(*, first, second):
    print("here we have a function that will only accept keyword arguments, no positional arguments allowed")
    print(f"{first} & {second}")
    print("\n")

keyword_only(second="Punishment", first="Crime")
