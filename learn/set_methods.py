# set is unordered, unindexed and immutable(but items can be added)
# One of the most unique thing about the is it ability to automatically remove duplicates

# ADD, adds an item to the set, will ignore if item is already present
set_a = set("still wakes the deep".split())
set_a.add("dark")
print(set_a)

# REMOVE/DISCARD, removes an item from the set
set_a.remove("dark")

# UPDATE, adds the contents of any iterable to the set
listt = ["test"]
set_a.update(listt)
print(set_a)

# POP, remove a random item
set_a.pop()

# ISSUBSET, check whether a given set is a subset of anther
set_b = {"still"}
print(set_b.issubset(set_a))
# or 
print(set_b <= set_a)

# ISSUPERSET, check whether a given set is super set of the other
set_b.issuperset(set_a)
# or
print(set_b >= set_a)


# UNION, return the union of 2 sets
print(set_a.union(set_b))
# or 
print(set_a | set_b)

# INTERSECTION, return another set that has the instersection content of the 2 sets operated on
print(set_a.intersection(set_b))
# or 
print(set_a & set_b)

# DIFFERENCE, return an set of the non common element of set-a when compared with set-b
print(set_a.difference(set_b))
# or 
print(set_a - set_b)

# SYMMETRIC_DIFFERENCE, return an set of all the non common element of both set-a and set-b
print(set_a.symmetric_difference(set_b))
# or 
print(set_a ^ set_b)
