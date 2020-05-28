""" Producer Consumer pattern using queue and ThreadPoolExecutor """
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

shared_queue = queue.Queue(maxsize=5)


def producer(index):
    count = 0
    for n in range(50):
        shared_queue.put(index * 100 + n)  # blocking
        count += 1
        time.sleep(0.001)
    return f"Producer{index}: produced {count}"


def consumer(index):
    count = 0
    for _ in range(50):
        print(f"Consumer{index}: {shared_queue.get()}")  # blocking
        count += 1
        time.sleep(0.002)
    return f"Consumer{index}: consumed {count}"


def submit_demo():
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(producer, i) for i in range(2)]
        futures += [pool.submit(consumer, i) for i in range(2)]
    print("Waiting for results")
    for f in futures:
        print(f.result())


def map_demo():
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = pool.map(producer, range(2))  # generator
        results2 = pool.map(consumer, range(2))
    print("Waiting for results")
    for r in results:
        print(r)
    for r in results2:
        print(r)


if __name__ == '__main__':
    # submit_demo()
    map_demo()
