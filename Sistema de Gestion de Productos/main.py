import os 
import platform
import time

from Products import (  ProductoElectronico, ProductoAlimenticio, GestionProdcutos)

def limpiar_pantalla(): 
    if platform.system() == "Windows": 
        os.system('cls')
    else: 
        os.system('clear')
    
"""    
def mostrar_menu(): 
    print("=================Menú de Gestión de Productos================")
    print('1. Agregar Producto Electronico')
    print('2. Agregar Producto Alimenticio')
    print('3. Buscar Producto por codigo')
    print('4. Actualizar Producto')
    print('5. Eliminar Producto por codigo')
    print('6. Mostrar todos los Producto')
    print('7. Salir')    
"""

def mostrar_menu(): 
    print("=================Menú de Gestión de Productos================")
    menu = ["1. Agregar Producto Electronico", "2. Agregar Producto Alimenticio", "3. Buscar Producto por codigo", "4. Actualizar Producto", "5. Eliminar Producto por codigo", "6. Mostrar todos los Producto", "7. Salir"]
    for i in menu: 
        time.sleep(0.5)
        print(i)
    time.sleep(1.5)
    print("")

def agregar_productos(gestion, tipo_producto): 
    try: 
        while True: 
            try: 
                codigo = int(input('Ingrese el codigo del producto: '))
                break
            except ValueError:
                print("")
                print('Tiene que ser un numero valido y entero intente nuevamente.')
                print("")
        nombre = input('Ingrese Nombre del producto: ')
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
        
        if tipo_producto == '1': 
            marca = input('Ingrese marca del producto: ')
            producto = ProductoElectronico(codigo, nombre, precio, cantidad, marca)
        elif tipo_producto == '2': 
            categoria = input('Ingrese la categoria del producto: ')
            producto = ProductoAlimenticio(codigo, nombre, precio, cantidad, categoria)
        else: 
            print('Tipo de producto no valido')
            input('Presione enter para continuar')
            return
            
        gestion.crear_producto(producto)
        input('Presione enter para continuar')
        
    except ValueError as e: 
        print(f'Error: {e}')
    except Exception as e: 
        print(f'Error inesperado: {e}')

def buscar_producto_por_codigo(gestion): 
    try: 
        codigo = input('Ingrese el codigo del producto a buscar: ')
        gestion.leer_producto(codigo)
        input('Presione enter para continuar')
    except ValueError as e: 
        print(f'Error: {e}')
    except Exception as e: 
        print(f'Error inesperado: {e}')

def actualizar_producto_precio(gestion):
    try: 
        codigo = input('Ingrese el codigo del producto para actualizar el precio: ')
        precio = float(input('Ingrese el precio nuevo del producto: '))
        gestion.actualizar_producto(codigo, precio)
        input('Presione enter para continuar')
    except ValueError as e: 
        print(f'Error: {e}')
    except Exception as e: 
        print(f'Error inesperado: {e}')

def eliminar_producto_por_codigo(gestion):
    try: 
        codigo = input('Ingrese el codigo del producto para eliminarlo: ')
        gestion.eliminar_producto(codigo)
        input('Presione enter para continuar')
    except Exception as e: 
        print(f'Error inesperado: {e}')
    
def mostrar_todos_los_productos(gestion):
    print('============Listado completo de los Productos================')
    for producto in gestion.leer_datos().values(): 
        if 'marca' in producto: 
            print(f'Nombre: {producto['nombre']} - Marca: {producto['marca']}')
        else: 
            print(f'Nombre: {producto['nombre']} - Categoria: {producto['categoria']}')
    print('=============================================================')
    input('Presione enter para continuar')

if __name__ == "__main__": 
    
    archivo_productos = 'registro_products.json'
    gestion_productos = GestionProdcutos(archivo_productos)
    
    while True: 
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opcion: ')
        
        if opcion == '1' or opcion == '2': 
            agregar_productos(gestion_productos, opcion)
        elif opcion == '3': 
            buscar_producto_por_codigo(gestion_productos)
        elif opcion == '4': 
            actualizar_producto_precio(gestion_productos)
        elif opcion == '5': 
            eliminar_producto_por_codigo(gestion_productos)
        elif opcion == '6': 
            mostrar_todos_los_productos(gestion_productos)
        elif opcion == '7': 
            print('Saliendo del programa')
            break
        else: 
            print('Opcion no valida')