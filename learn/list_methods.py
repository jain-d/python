# List methods in python, unlike string methods, list methods are applied directly alters the original list
state = ["still", "wakes", "the", "deep"]


# LENGTH, of the string
print(len(state))


# APPEND, adds a new entry to the list
state.append("part2")
print(state)


# INSERT, specify where to insert a string
state.insert(3, "dark")
print(state)            # dark will be inserted at index 3, anything pre-existing will be pushed after


# INDEX, find the index of where(which index) the item can be found at. Errors if element is not present
print(state.index("still"))


# EXTEND, used to add contents of another iterable inside the list
state = ["still", "wakes", "the", "deep"]
second_list = ["part", "2"]
state.extend(second_list)
print(state)

# any iterable, will also work with a tuple
state = ["still", "wakes", "the", "deep"]
second_tuple = ("part", "2")
state.extend(second_tuple)
print(state)


# REMOVE, removes a particular string from the list, error is the given string is not a part
state.remove("part")
print(state)


# POP, from the end, else removes a specified indiced item.
state.pop()
print(state)

state.pop(3)
print(state)


# COUNT, search for the specified string in the list, return the number of times is occurred
print(["still", "wakes", "the", "deep"].count("the"))
print(["still", "wakes", "the", "deep"].count("dark"))


# CLEAR, remove everything from the list
state.clear()
print(f'Empty list ->{state}')


# SORT, sorts the contents of the list alphanumerically in ascending order
state = "still wakes the deep".split(" ")
numeric_list = [43, 23, 34, 12, 82, 32]

state.sort()
numeric_list.sort()

print(state)
print(numeric_list)


# REVERSE, reveres the current order, first becomes last and last becomes first
print("still wakes the deep".split(" ").reverse())


# COPY, a shallow copy of another list
original_list = "still wakes the deep".split(" ")
state = original_list.copy()
original_list.append("part2")
print(state)

# can also be shallow copied like this
old_list = ["red", "green", "blue"]
new_list = list(old_list)


# DEEPCOPY vs SHALLOW COPY
# In this case where we have a list that contains nested list(or any mutable type)
list_one = [[5, 4, 3], [2, 1, 0]]
list_two = list_one.copy()
list_two = list(list_one)
list_two = list_one[::]
# a shallow copy here would mean that the list is copied, but the nested mutable types are the same.
# so any change in list list_one's inner lists would also appear in list_two
# shallow copy is outer structure are distinct different objects
# list_one is list_two          ✗
# but, inner mutables types are just references of the same object
# list_one[0] is list_two[0]    ✓


list_three = copy.deepcopy(list_one)
# here, with deep copy, not only do we have different outer structure, but also different inner structure as well
# list_three is list_one        ✗
# and also
# list_three[0] is list_one[0]  ✗
