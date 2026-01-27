class Stack:
    def __init__(self, starting_element=None):
        if starting_element:
            self.items = [starting_element,]
        else:
            self.items: list[str] = []

    def size(self) -> int:
        return len(self.items)

    def pop(self) -> str:
        if self.size() > 0:
            return self.items.pop()
        raise IndexError(f"The stack is empty.")

    def push(self, item: str):
        if item == "(" or item == ")":
            self.items.append(item)
        else:
            raise ValueError(f"can enter {item} in a paranthesis only stack.")

    def peek(self) -> str:
        if self.size() == 0:
            return None
        return self.items[-1]




def is_balanced(input_str) -> bool:
    stack = Stack()
    for entry in input_str:
        if entry == "(":
            stack.push(entry)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    if stack.size():
        return False
    return True



print(is_balanced("(()()"))
