# string

print("hoge" "fuga")  # 'hogefuga'

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
Bob''')  # no need to escape quotes and newlines

print()

# immutable
s = "hoge"
t = "hoge"
u = "ho"
v = str("hoge")
print(id(s))
print(id(t))
print(id(u))
u += "ge"
print(id(u))
print(id("hoge"))
print(id("ho" + "ge"))
print(id("ho" "ge"))
print(id(s) == id(t))  # => True
print(id(s) == id(u))  # => False
print(id(s) == id(v))  # => True
print(s == u)  # => True
print(s is u)  # => False

print()

print("hoge" + "fuga")
print("fefe" * 3)

# 文字コード変換
print(ord('🖖'))
print(chr(128406))
w = "ほげ"
print(len(w))
a = ascii(w)
print(a)
print(len(a))

# bytes
# b = bytes(w, encoding='utf-8')
b = w.encode(encoding='utf-8')
print(b)
print(len(b))
print(b.decode('utf-8'))

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
print('    Hello World    '.strip())
print('    Hello World    '.rstrip())
print('    Hello World    '.lstrip())

print()
print('Hello'.rjust(20))
print('Hello'.ljust(20, '*'))
print('Hello'.center(20, '='))

print()
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)

for name in names:
    print(name.ljust(biggest + 2, "-"))
for name in names:
    print(name.center(biggest + 2, "-"))
for name in names:
    print(name.rjust(biggest + 2, "-"))

print()

# searching
sample_str = "The quick brown fox jumps over the lazy dog"

# startsWith and endsWith functions
print(sample_str.startswith("The"))
print(sample_str.startswith("the"))
print(sample_str.endswith("dog"))

# the find and rfind functions
print(sample_str.find("the"))
print(sample_str.rfind("the"))
print("the" in sample_str)

# using replace
new_str = sample_str.replace("lazy", "tired")
print(new_str)

# counting instances of substrings
print(sample_str.count("over"))

# translate
trans_table = str.maketrans("abegilostz", "4636110572")
print(sample_str)
print(sample_str.translate(trans_table))
