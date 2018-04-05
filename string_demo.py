# string

# quotes
print("'hoge\nfuga'")
print('"hoge\nfuga"')

# raw string
print(r'That is Carol\'s cat.')
print(r"That is Carol's\n cat.")

print()

print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')  # no need escape quotes and newlines

print()

# immutable
s = "hoge"
t = "hoge"
u = "ho"
u += "ge"
v = str("hoge")
print(id(s))
print(id(t))
print(id(u))
print(id("hoge"))
print(id("ho" + "ge"))
print(id("fuga"))
print(id(s) == id(t))  # => True
print(id(s) == id(u))  # => False
print(id(s) == id(v))  # => True
print(s == u)  # => True
print(s is u)  # => False

print()

print("hoge" + "fuga")
print("fefe" * 3)

print()

# format
name = "Hoge Hoge"
machine = "HAL"
print('Nice to meet you %s. I am %s' % (name, machine))  # like C printf (legacy)
print('Nice to meet you {}. I am {}'.format(name, machine))
print('Nice to meet you {0}. I am {1}'.format(name, machine))
print("Nice to meet you {name}. I am {machine}".format(
    name=name, machine=machine))
print(f'Nice to meet you {name}. I am {machine}')  # 3.6

v = [1, -2, 3.3]
print('%4d%10d%10.3f' % (1, -2, 3.3))
# print('%4d%10d%10.3f' % (*v))  # NG
print('{0:4}{1:10}{2:10.3f}'.format(*v))
print('{:4}{:10}{:10.3f}'.format(*v))
print('{:>04}{:<10}{:10.3f}'.format(*v))

print()

# slice (substr)
spam = 'Hello world!'
print(spam)
print(spam[:])
print(spam[0])
print(spam[4])
print(spam[-1])  # 最後の文字
print(spam[-1:])  # 同上（listの場合とは違う）
print(spam[:-1])  # 最後の文字を除く
print(spam[0:5])  # 0 ~ 4番目の文字
print(spam[:5])  # 同上
print(spam[6:])  # 6番目以降の文字
print(spam[::2])  # 1文字置き
print(spam[::-1])  # 逆順

print()
print('Hello' in 'Hello World')
print('HELLO' in 'Hello World')
print('' in 'Hello World')
print('Howdy' not in 'Hello World')

print()

# methods
print("hello".islower())
print("Hello".isupper())
print("hello".upper())
print("Hello".lower())
print("Hello".swapcase())
print("hello World".capitalize())
print("hello world Straße".casefold())

print(' '.isspace())
print('　'.isspace())  # 全角スペース
print('\t'.isspace())
print('\n'.isspace())
print("hello".isalpha())
print("ｈｅｌｌｏ".isalpha())  # python3の文字列はUnicode
print("hello".isalnum())
print("123".isdigit())
print("123.5".isdigit())
print("123".isdecimal())
print("123.5".isdecimal())
print("123".isnumeric())
print("123.5".isnumeric())
print('This Is Title Case 123'.istitle())
print('This Is NOT Title Case 123'.istitle())

print()
print(', '.join(['cats', 'rats', 'bats']))
print("some,csv,values".split(","))
print("hello".replace("e", "a"))

print()
print('Hello'.rjust(20))
print('Hello'.ljust(20, '*'))
print('Hello'.center(20, '='))

print()
print('    Hello World    '.strip())
print('    Hello World    '.rstrip())
print('    Hello World    '.lstrip())
