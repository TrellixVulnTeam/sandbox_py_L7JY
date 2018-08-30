def banner(message, border='-'):
    line = border * (len(message) + 1)
    print(line)
    print(message)
    print(line)


if __name__ == '__main__':
    banner("Hoge Fuga FeFe!")
