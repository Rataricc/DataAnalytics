from Products import Products

class ProductoAlimenticio(Products):
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        super().__init__(codigo, nombre, precio, cantidad)
        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    def to_dict(self):
        data = super().to_dict()
        data['categoria'] = self.categoria
        return data

    def __str__(self):
        return f'{super().__str__()} - Categoria: {self.categoria}'
