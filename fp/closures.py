def new_collection(initial_docs: list[str]):
    copy_of_initial_docs = initial_docs.copy()
    def inner_func(some_str: str):
        nonlocal copy_of_initial_docs
        copy_of_initial_docs.append(some_str)
        return copy_of_initial_docs
    return inner_func

outer_caller = new_collection(["one", "two", "three"])

print(outer_caller("four"))
print(outer_caller("five"))


