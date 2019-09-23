from .abs_auto import AbsAuto


class ChevySpark(AbsAuto):
    def start(self):
        print('Chevy Spark running efficiently.')

    def stop(self):
        print('Chevy Spark shutting down.')


class ChevyCamaro(AbsAuto):
    def start(self):
        print('Chevy Camaro V8 sounding awesome!')

    def stop(self):
        print('Chevy Camaro shutting down.')


class CadillacCTS(AbsAuto):
    def start(self):
        print('Cadillac CTS purring luxuriously.')

    def stop(self):
        print('Cadillac CTS shutting down.')
