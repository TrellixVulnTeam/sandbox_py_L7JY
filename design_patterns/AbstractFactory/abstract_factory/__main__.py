from factories import FordFactory, GMFactory

for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()
    car = factory.create_sport()
    car.start()
    car.stop()
    car = factory.create_luxury()
    car.start()
    car.stop()
