import asyncio

async def run_timer(number):
    while True:
        await asyncio.sleep(0.5)
        if number == 0:
            break

        print(f'\033[94m{number}\033[0m')
        number -= 1


async def another_runner():
    for _ in range(3):
        await asyncio.sleep(0.5)
        print("\033[31m.\033[0m")


async def main():
    await asyncio.gather(run_timer(3), another_runner())


asyncio.run(main())
