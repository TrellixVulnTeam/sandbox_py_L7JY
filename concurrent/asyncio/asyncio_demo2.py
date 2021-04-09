import asyncio
import random


async def get_content(n):
    print(f'start: {n}')
    await asyncio.sleep(random.randint(1, 3))  # レスポンスタイムが違うことをシミュレート
    print(f'end: {n}')
    return n


async def coro_old():
    tasks = [asyncio.ensure_future(get_content(x)) for x in range(10)]
    return await asyncio.gather(*tasks)  # asyncio.gather()の戻り値の順番は保証される


async def coro():
    """Python3.7+"""
    tasks = [asyncio.create_task(get_content(x)) for x in range(10)]
    return await asyncio.gather(*tasks)


def main_old():
    loop = asyncio.get_event_loop()
    v = loop.run_until_complete(coro_old())
    loop.close()
    return v


def main():
    """Python3.7+"""
    v = asyncio.run(coro())
    return v


if __name__ == "__main__":
    print(main())
