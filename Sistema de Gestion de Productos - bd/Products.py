class Products:

    def __init__(self, codigo, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = self.validar_precio(precio)
        self.__cantidad = self.validar_cantidad(cantidad)
        self.__codigo = self.validar_codigo(codigo)

    # Getters
    @property
    def precio(self):
        return self.__precio

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def nombre(self):
        return self.__nombre.capitalize()

    @property
    def codigo(self):
        return self.__codigo

    # Setters
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = self.validar_codigo(nuevo_codigo)

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = self.validar_cantidad(nueva_cantidad)

    def validar_precio(self, precio):
        try:
            precio_num = float(precio)
            if precio_num < 0:
                raise ValueError("El precio debe ser un numero positivo")
            return precio_num
        except ValueError:
            raise ValueError("El precio debe ser un numero valido")

    def validar_cantidad(self, cantidad):
        try:
            cantidad_num = int(cantidad)
            if cantidad_num < 0:
                raise ValueError("La cantidad debe ser un numero positivo")
            return cantidad_num
        except ValueError:
            raise ValueError("La cantidad debe ser un numero valido")

    def validar_codigo(self, codigo):
        try:
            codigo_num = int(codigo)
            if len(str(codigo_num)) <= 2:
                raise ValueError(
                    "El codigo debe ser un numero positivo y mayor a 3")
            return codigo_num
        except ValueError:
            raise ValueError("El codigo debe ser un numero valido")

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Codigo: {self.codigo}"