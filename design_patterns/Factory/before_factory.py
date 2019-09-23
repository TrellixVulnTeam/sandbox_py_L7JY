class ChevyVolt(object):
    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')


class FordFocus(object):
    def start(self):
        print('Cool Ford Focus running smoothly.')

    def stop(self):
        print('Ford Focus shutting down.')


class JeepSahara(object):
    def start(self):
        print('Jeep Saraha running ruggedly.')

    def stop(self):
        print('Jeep Saraha shutting down.')


class NullCar(object):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s."' % self._carname)

    def stop(self):
        pass


def getcar(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFocus()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)


if __name__ == '__main__':
    for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
        car = getcar(carname)
        car.start()
        car.stop()
