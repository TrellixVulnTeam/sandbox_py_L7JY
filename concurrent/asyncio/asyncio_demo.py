import asyncio
import time


async def get_content(n):
    """ネットワークI/Oなどの時間の掛かる処理の代わり"""
    time.sleep(3)
    return n


async def coro(n):
    content = await get_content(n)  # この行でcoro()は中断される
    return content


def main_old():
    loop = asyncio.get_event_loop()
    v = loop.run_until_complete(coro("done"))
    loop.close()
    return v


def main():
    """Python3.7+"""
    v = asyncio.run(coro("done"))
    return v


if __name__ == "__main__":
    print(main())
