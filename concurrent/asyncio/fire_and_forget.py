import asyncio
import time


def get_content(n):
    """ネットワークI/Oなどの時間の掛かる処理の代わり"""
    time.sleep(3)
    print("after sleep in get_content()")
    return n


def main():
    loop = asyncio.get_event_loop()
    v = loop.run_in_executor(None, get_content, "done")
    return v


if __name__ == "__main__":
    main()
    print("after main()")
