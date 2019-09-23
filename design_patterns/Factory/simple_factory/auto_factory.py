from inspect import getmembers, isclass, isabstract
import autos


class AutoFactory(object):
    autos = {}  # Key = car model name, Value = class for the car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        # [('name', 'class')]
        classes = getmembers(autos,
                             lambda m: (isclass(m)
                                        and not isabstract(m)
                                        and issubclass(m, autos.AbsAuto))
                             )
        self.autos.update(classes)

    # 共通化しているので、インスタンス化に当たって柔軟性がなくなる
    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return autos.NullCar(carname)
