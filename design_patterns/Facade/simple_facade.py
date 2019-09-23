import abc


class AbsFacade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass


class JsonFacade(AbsFacade):
    def load(self):
        # load from JSON ...
        return {'data': 'JSON'}

    def save(self):
        # save to JSON ...
        pass


class XmlFacade(AbsFacade):
    def load(self):
        # load from XML ...
        return {'data': 'XML'}

    def save(self):
        # save to XML ...
        pass


CONFIG = {
    'JSON': JsonFacade,
    'XML': XmlFacade,
}


# Factory method
def create_facade(provider):
    return CONFIG[provider]()


if __name__ == '__main__':
    facade = create_facade('JSON')
    print(facade.load())

    facade = create_facade('XML')
    print(facade.load())
