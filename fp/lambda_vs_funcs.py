# Lambda vs Helper Functions
import dis

print('--- Lambda ---')


def f(x): return x.g(lambda x: x.good, lambda x: x.member)


dis.dis(f)

print()
print('--- Local Functions ---')


def f(x):
    def l1(x): return x.good

    def l2(x): return x.member

    return x.g(l1, l2)


dis.dis(f)

print()
print('--- Helper Functions ---')


def l1(x): return x.good


def l2(x): return x.member


def f(x): return x.g(l1, l2)


dis.dis(f)
