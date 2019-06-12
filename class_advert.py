import json
from keyword import iskeyword

from avito_case.json_objects import data


class ColorizeMixin:
    def __repr__(self):
        return f'\033[1;32;{self.repr_color_code}m {self.title} | {self.price} P'


class Attributes:
    def __init__(self, json_dict: dict):
        for k, v in json_dict.items():
            if k == 'price':
                self.price = v
            else:
                if isinstance(v, dict):
                    value = Attributes(v)
                else:
                    k = f'{k}_' if iskeyword(k) else k
                    value = v

                self.__dict__[k] = value


class Advert(ColorizeMixin, Attributes):
    repr_color_code = 32

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price must be greater or equal than 0')

        self._price = value




a = Advert(json.loads(data.iphone_str))

print(a.def_)
# a.price = 100

# print(a.blue, a.location, a.end_clr)
