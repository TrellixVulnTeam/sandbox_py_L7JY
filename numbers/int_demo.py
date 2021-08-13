# int: unlimited precision signed integer
# very different from another languages
print(0b10)
print(0o10)
print(0x10)

# base conversion
print(bin(42))
print(oct(42))
print(hex(42))
print(hex(42)[2:])
print(int('2a', base=16))
print(int('0o664', base=8))
print(int('0o664', base=0))
print(int('acghd', base=18))
print(int('0b111000', base=2))

print()

# Division demo
print(3 / 2)  # => 1.5
print(3 // 2)  # => 1
print(-3 / 2)  # => -1.5
print(-3 // 2)  # => -2 : "floor division"
print(4.5 // 2)  # => 2.0 : not int
