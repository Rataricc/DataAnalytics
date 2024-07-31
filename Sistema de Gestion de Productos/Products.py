import json

class Products: 
    
    def __init__(self, codigo, nombre, precio, cantidad): 
        self.__nombre = nombre
        self.__precio = self.validar_precio(precio)
        self.__cantidad = self.validar_cantidad(cantidad)
        self.__codigo = self.validar_codigo(codigo)
    
    #Getters
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
    
    #Setters
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
                    raise ValueError("El codigo debe ser un numero positivo y mayor a 3")
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
 
        
class GestionProdcutos: 
    def __init__(self, archivo):
        self.archivo = archivo
        
    def leer_datos(self): 
        try:
            with open(self.archivo, 'r') as file: 
                datos = json.load(file)
        except FileNotFoundError: 
            return {}
        except Exception as error: 
            raise Exception(f'Error a leer datos del archivo: {error}')
        else: 
            return datos

    def guardar_datos(self, datos): 
        try: 
            with open(self.archivo, 'w') as file: 
                json.dump(datos, file, indent=4)
        except IOError as error: 
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error: 
            print(f'Error inesperado: {error}')
    
    def crear_producto(self, producto): 
        try: 
            datos = self.leer_datos()
            codigo = producto.codigo
            if not str(codigo) in datos.keys(): 
                datos[codigo] = producto.to_dict()
                self.guardar_datos(datos)
                print(f'Producto {producto.nombre} {producto.codigo} creado correctamente')
            else: 
                print(f'Producto con codigo {codigo} ya existente')
        except Exception as error: 
            print(f'Error al intentar crear el producto: {error}')
    
    def leer_producto(self, codigo): 
        try:
            datos = self.leer_datos() 
            if codigo in datos: 
                producto_data = datos[codigo]
                if 'marca' in producto_data: 
                    producto = ProductoElectronico(**producto_data)
                else: 
                    producto = ProductoAlimenticio(**producto_data)
                print(f'Porducto encontrado con codigo: {codigo}')
                print(f'Porducto: {producto}')
                return producto
            else: 
                print(f'Porducto no encontrado con el codigo: {codigo}')
        except Exception as e:
            print(f'Error al intentar leer el producto: {e}')
            
    def actualizar_producto(self, codigo, nuevo_precio): 
        try: 
            datos = self.leer_datos()
            if str(codigo) in datos.keys(): 
                datos[codigo]['precio'] = nuevo_precio #Hacer validaciones...
                self.guardar_datos(datos)
                print(f'Precio actualizado correctamente para el prodcuto: {codigo}')
            else: 
                print(f'No se encontro el prodcuto con el codigo: {codigo}')
        except Exception as e: 
            print(f'Error al intentar actualizar el producto: {e}')
    
    def eliminar_producto(self, codigo): 
        try: 
            datos = self.leer_datos()
            if str(codigo) in datos.keys(): 
                del datos[codigo]
                self.guardar_datos(datos)
                print(f'Producto eliminado correctamente con codigo: {codigo}')
            else: 
                print(f'No se encontro el prodcuto con el codigo: {codigo}')
        except Exception as e: 
            print(f'Error al intentar eliminar el producto: {e}')