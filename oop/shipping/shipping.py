import iso6346


def _c_to_f(celsius):
    return celsius * 9 / 5 + 32


def _f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):  # cls is polymorphic
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents, *args, **kwargs):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(  # polymorphic static method
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return self._calc_volume()  # delegate

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 10

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return _c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = _f_to_c(value)

    # @property
    # def volume_ft3(self):
    #     return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    # propertyをoverrideするのではなく、normal methodをoverride （Template Method Pattern）
    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0

    # getterはそのまま継承

    # @RefrigeratedShippingContainer.celsius.setter
    # def celsius(self, value):
    #     if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
    #         raise ValueError("Temperature too cold!")
    #     RefrigeratedShippingContainer.celsius.fset(self, value)

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)


if __name__ == '__main__':
    r1 = RefrigeratedShippingContainer.create_empty('YML', 20, celsius=-20.0)
    print(r1.celsius)
    print(r1.fahrenheit)
    r1.fahrenheit = -10.0
    print(r1.celsius)

    h1 = HeatedRefrigeratedShippingContainer.create_empty('YML', 40, celsius=-40.0)

    r2 = RefrigeratedShippingContainer.create_empty('MAE', 20, celsius=7.0)
