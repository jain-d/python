#!/usr/bin/env python3
import random
import asyncio
import sys

async def main_func():
    times = 1 if not sys.argv[-1].isdigit() else int(sys.argv[-1])
    while times:
        season = random.randint(1, 9)
        episode: int

        match season:
            case 1:
                episode = random.randint(1, 6)
            case 2:
                episode = random.randint(1, 22)
            case 3 | 9:
                episode = random.randint(1, 25)
            case 4:
                episode = random.randint(1, 14)
            case 5 | 6 | 7:
                episode = random.randint(1, 26)
            case 8:
                episode = random.randint(1, 24)

        print(f"\n\t\033[32mS{season}\033[33mE{episode}")
        if times > 2:
            await asyncio.sleep(0.5)
        times -= 1

asyncio.run(main_func())
