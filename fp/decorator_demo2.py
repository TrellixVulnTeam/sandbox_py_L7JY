def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return 'Tromsø'


class Trace:
    """callable decorator"""
    def __init__(self, enabled=True):
        self.enabled = enabled  # output on/off

    def __call__(self, f):
        """decorator method"""
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()
# tracer = Trace(enabled=False)


@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'


class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        """decorated method"""
        return name + self.suffix


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


if __name__ == '__main__':
    print(northern_city())

    l = [1, 2, 3]
    l = rotate_list(l)
    print(l)
    l = rotate_list(l)
    print(l)
    tracer.enabled = False
    l = rotate_list(l)
    print(l)

    print(norwegian_island_maker("Hoge"))

    im = IslandMaker("_o_")
    print(im.make_island("FeFe"))
