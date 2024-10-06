import os
import platform
import time
from dotenv import load_dotenv
from ProdcutoElectronico import ProductoElectronico
from ProductoAlimenticio import ProductoAlimenticio
from GestionProductos import GestionProductos
#from Products import (ProductoElectronico,ProductoAlimenticio, GestionProductos)


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu():
    print("=================Menú de Gestión de Productos================")
    menu = [
        "1. Agregar Producto Electrónico",
        "2. Agregar Producto Alimenticio",
        "3. Buscar Producto por código",
        "4. Actualizar Producto",
        "5. Eliminar Producto por código",
        "6. Mostrar todos los Productos",
        "7. Salir"
    ]
    for opcion in menu:
        time.sleep(0.5)
        print(opcion)
    print("")


def agregar_producto(gestion, tipo_producto):
    try:
        while True: 
            try: 
                codigo = int(input('Ingrese el codigo del producto: '))
                break
            except ValueError:
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        nombre = input('Ingrese el nombre del producto: ')
        while True: 
            try:
                precio = int(input('Ingrese precio del producto: '))
                break
            except ValueError: 
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        while True: 
            try:
                cantidad = int(input('Ingrese cantidad que hay del producto: '))
                break
            except ValueError:
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        if tipo_producto == 'electronico':
            marca = input('Ingrese la marca del producto electrónico: ')
            producto = ProductoElectronico(codigo, nombre, precio, cantidad, marca)
        elif tipo_producto == 'alimenticio':
            categoria = input('Ingrese la categoría del producto alimenticio: ')
            producto = ProductoAlimenticio(codigo, nombre, precio, cantidad, categoria)

        gestion.crear_producto(producto)
        print(producto)
        print(f"Producto {tipo_producto} agregado con éxito.")
        input('Presione enter para continuar')

    except ValueError as e:
        print(f"Error al ingresar los datos: {e}")


def actualizar_prodcuto_por_codigo(gestion):
    while True: 
        try: 
            codigo = int(input('Ingrese el código del producto a actualizar: '))
            break
        except ValueError:
            print("")
            print('Tiene que ser un numero valido y entero intente nuevamente.')
            print("")
    producto = gestion.leer_producto(codigo)
    if producto:
        print(f"Producto encontrado: {producto}")
        while True: 
            try:
                nuevo_precio = float(input('Ingrese el nuevo precio para el producto: '))
            except ValueError: 
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        producto_actualizado = gestion.actualizar_producto(codigo, nuevo_precio)
        if producto_actualizado:
            print("Producto actualizado:")
            print(f"Código: {producto_actualizado[0]}, Nombre: {producto_actualizado[1]}, Precio: {producto_actualizado[2]}")
        else:
            print("No se pudo actualizar el producto.")
    else:
        print("Producto no encontrado.")

    input("Presione enter para continuar: ")


def buscar_producto_por_codigo(gestion): 
    while True: 
        try: 
            codigo = int(input('Ingrese el código del producto a buscar: '))
            break
        except ValueError: 
            print("")
            print('Tiene que ser un numero valido y entero intente nuevamente.')
            print("")
    producto = gestion.leer_producto(codigo)
    if producto:
        print(producto)
    input("Presione enter para continuar: ")


def eleminar_prodcuto_por_codigo(gestion): 
    try: 
        while True: 
            try: 
                codigo = int(input('Ingrese el código del producto a eliminar: '))
                break
            except ValueError: 
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        gestion.eliminar_producto(codigo)
        print("Prodcuto eliminado exitosamente")
        input("Presione enter para continuar: ")
    except Exception as error: 
        print(f"Error al eliminar el producto: {error}")


def traer_todos_los_productos(gestion): 
    productos, columnas = gestion.leer_datos()
    for p in productos:
        for i, valor in enumerate(p):
            print(f"{columnas[i]}: {valor}")
        print('-' * 40) 
    input('Presione enter para continuar: ')


def main():
    load_dotenv()
    gestion = GestionProductos()

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregar_producto(gestion, 'electronico')
        elif opcion == '2':
            agregar_producto(gestion, 'alimenticio')
        elif opcion == '3':
           buscar_producto_por_codigo(gestion)
        elif opcion == '4':
           actualizar_prodcuto_por_codigo(gestion)
        elif opcion == '5':
            eleminar_prodcuto_por_codigo(gestion)
        elif opcion == '6':
            traer_todos_los_productos(gestion)
        elif opcion == '7':
            gestion.cerrar_conexion()
            print("Saliendo...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")
            input("Presione enter para continuar: ")


if __name__ == '__main__':
    main()