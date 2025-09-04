class A:
    def __init__(self, one):
        self.one = one

    def __str__(self):
        return f'this is A'

class A1:
    __slots__ = ["two"]
    def __init__(self, two):
        self.two = two

    def method(self):
        print("A1 method")

    def __str__(self):
        return f"this is A1"

a1 = A1(5)
a1.__dict__["three"] = 9
print(a1)
print(a1.three)
print(a1.__dict__)

a = A(9)

print("\n")
print(a)
print(vars(a))
