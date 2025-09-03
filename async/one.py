import asyncio

async def run_timer(number):
    while True:
        await asyncio.sleep(0.5)
        if number == 0:
            break

        print(number)
        number -= 1


number = int(input("How long? "))

asyncio.run(run_timer(number))
