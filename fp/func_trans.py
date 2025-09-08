import asyncio
import random

def random_ops():
    def add(x, y):
        return x + y
    
    def mul(x, y):
        return x * y

    if random.randint(1, 2) % 2 == 0:
        return add
    return mul


async def main():
    for _ in range(5):
        some_operation = random_ops()
        print(some_operation(3, 4))
        await asyncio.sleep(0.25)



def mul(s, p):
    return s * p

def modifier(func):
    def wrapper_func(x):
        return func(x, x)
    return wrapper_func

modified_add = modifier(mul)

print(modified_add(4))

