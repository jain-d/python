import asyncio

async def func_one():
    for _ in range(5):
        print("\033[31mawaits 0.1 second\033[0m")
        await asyncio.sleep(0.1)

async def func_two():
    n = 3
    while n > 0:
        to_display = list("hello World, how are you doing, I hope you are doing well.")
        message = ""
        for index, character in enumerate(to_display):
            if index % 2 != 0 and character.islower():
                message += chr(ord(character) - 32)
            else:
                message += character
            print(f"{index}. {message}")
        for _ in range(index):
            print(message)
        await asyncio.sleep(0.1)
        n -= 1

async def main():
    await asyncio.gather(func_one(), func_two())


asyncio.run(main())
