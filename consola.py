import os
from parte_1 import get_indexes
from parte_2 import get_media
from parte_2 import get_staircase

continuar = True

while continuar:
    os.system("cls")
    print("""\t---------------- RETOS ----------------
        -------- Prueba técnica Summa ---------
        1. Devolver índices de números que sumados dan un número específico
        2. Presentar la funcionalidad 1 de los tres agentes (A, B, C)
        3. Presentar la funcionalidad 2 de los tres agentes (A, B, C)
        4. Salir
        ---------------------------------------""")
    try:
        ret = int(input("Ingrese el número de reto que desea evaluar: "))
        if ret == 1:
            continuar = get_indexes()
        elif ret == 2:
            x = input('Ingrese un arreglo de números reales separados por coma y sin espacios: ').split(',')
            lista_num = [int(item) for item in x]
            continuar = get_media(lista_num)
        elif ret == 3:
            n = int(input('Ingrese un número entero entre 1 y 99: '))
            if 0 < n < 100:
                continuar = get_staircase(n)
            else: 
                print('Escriba un número entre 1 y 99')
        elif ret == 4:
            continuar = False
        input("Presione enter para continuar...")
    except:
        print("No ingresó un número, vuelva a intentar")
        input("Presione enter para continuar...")
        continuar = True