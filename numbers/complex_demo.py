# complex
import cmath

print(2j)
print(type(3 + 4j))
print(complex(-2, 3))
print(complex('-2+3j'))
# print(complex('-2 + 3j'))  # NG

c = 3 + 5j
print(c.real, c.imag)  # float
print(c.conjugate())

print(cmath.sqrt(-1))
print(cmath.phase(1 + 1j))  # x-axis: 1, y-axis: 1 => 0.785 rad (45°)
print(abs(1 + 1j))
print(abs(complex(0, -5)))

modulus, phase = cmath.polar(1 + 1j)
print(modulus, phase)
print(cmath.rect(modulus, phase))  # float
