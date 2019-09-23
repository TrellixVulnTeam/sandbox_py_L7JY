from .abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    def start(self):
        print('Ford Fiesta running cheaply.')

    def stop(self):
        print('Ford Fiestashutting down.')


class FordMustang(AbsAuto):
    def start(self):
        print("Ford Mustang roaring and ready to go!")

    def stop(self):
        print('Ford Mustang shutting down.')


class LincolnMKS(AbsAuto):
    def start(self):
        print('Lincoln MKS running smoothly.')

    def stop(self):
        print('Lincoln MKS shutting down.')
