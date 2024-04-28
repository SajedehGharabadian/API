import time 
import random
import asyncio

async def get():
    print("Get file started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"Get file ended in {r} seconds")

async def extract():
    print("Extract file started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"Extract file ended in {r} seconds")

async def download():
    print("Download started")
    await get()
    await extract()
    print(f"Download ended")

async def printer():
    print("Print started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"Print ended in {r} seconds")

async def ai_audio():
    print("AI audio started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"AI audio ended in {r} seconds")

async def ai_video():
    print("AI video started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"AI video ended in {r} seconds")

def mix():
    print("mix started")
    r = random.randint(0,10)
    time.sleep(r)
    print(f"mix ended in {r} seconds")

async def ai():
    print("AI started")
    asyncio.gather(ai_audio(),ai_video())
    mix()
    print(f"AI ended")

async def main():
    await asyncio.gather(download(),printer(),ai())


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")