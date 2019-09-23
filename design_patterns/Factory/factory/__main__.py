from factories import load_factory

for factory_name in 'ChevyFactory', 'JeepFactory', 'FordFactory', 'HogeFactory':
    factory = load_factory(factory_name)
    car = factory.create_auto()
    car.start()
    car.stop()
