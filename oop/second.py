class Testing:
    def __init__(self, identity):
        self.identity = identity

    def __str__(self) -> str:
        return f"Custom Object SIGNATURE, {self.identity}"

obj_one = Testing("first")

obj_two = Testing("second")

print(obj_one)
