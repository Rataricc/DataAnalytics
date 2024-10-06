from Products import Products

class ProductoElectronico(Products):
    def __init__(self, codigo, nombre, precio, cantidad, marca):
        super().__init__(codigo, nombre, precio, cantidad)
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        return self.marca

    def to_dict(self):
        data = super().to_dict()
        data['marca'] = self.marca
        return data

    def __str__(self):
        return f'{super().__str__()} - Marca: {self.marca}'
