print("Beginning Program")
print("Importing Libaries")

import os
import asyncio
import time
os.system('cls')

print("Importing Libaries Complete")
print("Preparing.")
print("Preparing..")
print("Preparing...")

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def loading():
    """
    This function displays a loading animation until loaded is True.
    """
    import sys
    import random
    import datetime
    loaded = False
    while not loaded:
        print("Loading.")
        asyncio.wait(0.5)
        os.system('clear')
        print("Loading..")
        asyncio.wait(0.5)
        os.system('clear')
        print("Loading...")
        asyncio.wait(0.5)
        os.system('clear')
        loaded = await preperation()

async def preperation():
    """
    This function prepares the program.
    """
    for _ in range(1, 6):
        print("hi")
        await asyncio.sleep(1)
    loaded = True
    return loaded

async def main():
    await asyncio.gather(loading())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
async def preperation():
    for i in range(1,6):
        print("hi")
        await asyncio.sleep(1)
    loaded = True
    return loaded
