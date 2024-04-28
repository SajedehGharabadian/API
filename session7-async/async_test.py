import asyncio
import time
import random

async def marriage(i):
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"{i} married after {r} years")


async def main():
    await asyncio.gather(marriage("mohamad"),marriage("gholi"),marriage("goli"),marriage("alex"))


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")

    