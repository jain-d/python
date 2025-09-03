import asyncio

async def unlimited_counts():
    try:
        number = 0
        while True:
            await asyncio.sleep(0.5)
            number += 1
            print(f"\033[94m{number}\033[0m")
    except asyncio.CancelledError:
            print(f' === \033[93mbye\033[0m ===')
            raise

async def stopper(task):
    print('\033[32mstarted waiting\033[0m')
    await asyncio.sleep(5)
    print('\033[31mwaits over!\033[0m')
    task.cancel()

async def main():
    task_one = asyncio.create_task(unlimited_counts())
    task_two = asyncio.create_task(stopper(task_one))
    try:
        await task_one
        await task_two
    except asyncio.CancelledError:
        pass

asyncio.run(main())

