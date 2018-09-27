class OneShotDict(dict):
    """One-shot dict"""

    def __init__(self, existing=None):
        super().__init__()
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise ValueError("Cannot assign to existing key {!r}".format(key))
        super().__setitem__(key, value)


if __name__ == '__main__':
    d = OneShotDict()
    d['a'] = 65
    d['b'] = 66
    d['a'] = 32
    d['c'] = 777
