# Instrucción: Dada un arreglo de enteros, devuelva los índices de los dos números de modo que se sume un número específico.
# Nota: Asuma que en cada entrada se tendrá exactamente una solución, y no puede usar el mismo elemento dos veces.

from itertools import combinations

def get_indexes():
    """
    Get_indexes

    Args:
        Esta función no recibe argumentos en el llamado
        
    Returns:
        Esta función retorna una lista con los índices de los 2 números que sumados dan como resultado el número deseado
    """
    
    try:
        x = input('Ingrese un arreglo de números enteros separados por coma y sin espacios: ').split(',')
        y = int(input('Ingrese el número objetivo: '))
    
        # Crea una lista a partir de los números ingresados
        numeros = [int(item) for item in x]
        
        # Genera todas las combinaciones de 2 números posibles usando la lista de números
        combinaciones = [i for i in combinations(numeros,2)]
        
        # Suma los 2 números en cada una de las combinaciones y verifica si el número objetivo se encuentra en esas sumas
        found = False
        for i in combinaciones:
            if (i[0] + i[1] == y):
                print(f'Los indices de los números que sumados dan {y} son [{numeros.index(i[0])}, {numeros.index(i[1])}]')
                found = True
                break
        if not found:    
            print('Con los números de la lista no se puede obtener el número deseado')

    except Exception as e:
        print("Debes ingresar números enteros")
        #print(e)
    
    return True

#get_indexes()