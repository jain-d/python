import asyncio

async def run_timer(number):                                # 2. Execution Starts here
    while True:
        await asyncio.sleep(0.5)                            # 3/7. the coroutine yields control back to the Event LOOP goes to next task in queue/sends to #8
        if number == 0:                                     # 6. Execution resumes from here
            break

        print(f'\033[94m{number}\033[0m')
        number -= 1


async def another_runner():                                 # 4/8. Since another_runner was in task queue, we start the execution here/resumes from #7
    for _ in range(3):
        await asyncio.sleep(0.5)                            # 5. Now this thread sleeps again, giving the execution focus to the next item in taskQueue
        print("\033[31m.\033[0m")


# ==== MAIN ENTRY POINT ====
async def main():
    await asyncio.gather(run_timer(3), another_runner())    # <== 1. The Event Loop schedule 2 coroutines, first one being run_timer


asyncio.run(main())


# NOTE: All of this is entirely single threaded, with task yielding back control at await points.
