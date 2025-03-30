import asyncio
import dotenv
import os

dotenv.load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")

async def async_fn(message: str, delay: int)->None:
    """
    async funtion
    """
    print(f"Starting:{message}")
    await asyncio.sleep(delay)
    print(f"Finished: {message}")

async def main():
    task1 =asyncio.create_task(async_fn('1st task',2))
    task2= asyncio.create_task(async_fn('2nd task',3))
    task3 = asyncio.create_task(async_fn('3rd_task',2))

    #wait for all tsk to complete
    await asyncio.gather(task1,task2,task3)

if __name__=="__main__":
    asyncio.run(main())
    print(gemini_api_key)



