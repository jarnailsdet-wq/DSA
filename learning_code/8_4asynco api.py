#
import time

# def check_api():
#     print("Checking API...")
#     time.sleep(2)  # Simulate network delay
#     print("API is up!")
    
# check_api()
# check_api()
# check_api()


import asyncio

async def check_api():
    print("Checking API...")
    await asyncio.sleep(2)  # Simulate network delay
    print("API is up!")
    
async def main():
    await asyncio.gather(check_api(), check_api(), check_api())

asyncio.run(main())