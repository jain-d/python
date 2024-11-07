# tuples are a immutable collection types, meaning once created can not be modified, unless...

tup = tuple("still wakes the deep in the ocean".split(" "))


# COUNT, gives us a count of the number of times a the given value has appeared
print(tup.count("the"))


# INDEX, give the index at which the value is present, if the value is not present, throw error
print(tup.index("the"))


# we can delete a tuple from memory with del keyword
del tup


# Tuple math
# Addition, this is a cheeky way of adding item to a tuple, we smash it another tuple
tup = tuple(("still", "wakes", "the"))
tup += tuple(("deep",))

# Multiplication, this just multiplies the current existing contents in the tuple to appear that many times
tup *= 2
