# Native concurrency with asyncio
import asyncio
import time


async def my_task():
    time.sleep(1)  # to hold for 1 seconds
    print("Processing Task")


async def my_task_generator():
    for i in range(5):
        asyncio.ensure_future(my_task())
        print(asyncio.Task.all_tasks())  # For list of pending tasks


# initiated loop-
initiate_loop = asyncio.get_event_loop()

# running the task until it gets over-
initiate_loop.run_until_complete(my_task_generator())

# Signal to check if all tasks are completed
print("Completed All Tasks")

# Safely Closing loop
initiate_loop.close()
