import asyncio

async def delayed_print():
    await asyncio.sleep(0.4)
    print("\tdelayed text")

async def test_async():
    print("\t\033[33minitialized\033[0m")
    task = asyncio.create_task(delayed_print())
    print("\t\033[32mcompleted\033[0m")
    await task

asyncio.run(test_async())
