from db_connection import get_db_connection
from ProdcutoElectronico import ProductoElectronico
from ProductoAlimenticio import ProductoAlimenticio

class GestionProductos:
    def __init__(self):
       self.conn = get_db_connection()

    def leer_datos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM productos')
            datos = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
        except Exception as error:
            raise Exception(
                f'Error al leer datos de la base de datos: {error}')
        else:
            return datos, columnas
        finally:
            cursor.close()

    def crear_producto(self, producto):
        cursor = self.conn.cursor()

        cursor.execute('''
            INSERT INTO productos (codigo, nombre, precio, cantidad)
            VALUES (%s, %s, %s, %s)
        ''', (producto.codigo, producto.nombre, producto.precio, producto.cantidad))

        if isinstance(producto, ProductoElectronico):
            cursor.execute('''
                INSERT INTO prodcutoElectronico (codigo, marca)
                VALUES (%s, %s)
            ''', (producto.codigo, producto.marca))

        elif isinstance(producto, ProductoAlimenticio):
            cursor.execute('''
                INSERT INTO prodcutoAlimenticio (codigo, categoria)
                VALUES (%s, %s)
            ''', (producto.codigo, producto.categoria))

        self.conn.commit()
        cursor.close()

    def leer_producto(self, codigo):
        cursor = self.conn.cursor()

        cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,))
        producto = cursor.fetchone()

        if producto:
            cursor.execute('''
                SELECT marca FROM prodcutoElectronico WHERE codigo = %s
            ''', (codigo,))
            marca = cursor.fetchone()

            cursor.execute('''
                SELECT categoria FROM prodcutoAlimenticio WHERE codigo = %s
            ''', (codigo,))
            categoria = cursor.fetchone()

            cursor.close()

            if marca:
                producto = ProductoElectronico(
                    producto[0], producto[1], producto[2], producto[3], marca[0])
            elif categoria:
                producto = ProductoAlimenticio(
                    producto[0], producto[1], producto[2], producto[3], categoria[0])

            return producto
        else:
            print(f"No se encontró el producto con código {codigo}.")
            return None

    def actualizar_producto(self, codigo, nuevo_precio):
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE productos SET precio = %s WHERE codigo = %s
            ''', (nuevo_precio, codigo))
            self.conn.commit()
            cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,))
            producto_actualizado = cursor.fetchone()
            return producto_actualizado
        except Exception as error:
            raise Exception(f'Error al actualizar el producto: {error}')
        finally:
            cursor.close()

    def eliminar_producto(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute(
            'DELETE FROM prodcutoElectronico WHERE codigo = %s', (codigo,))
        cursor.execute(
            'DELETE FROM prodcutoAlimenticio WHERE codigo = %s', (codigo,))
        cursor.execute('DELETE FROM productos WHERE codigo = %s', (codigo,))
        self.conn.commit()
        cursor.close()

    def cerrar_conexion(self):
        self.conn.close()