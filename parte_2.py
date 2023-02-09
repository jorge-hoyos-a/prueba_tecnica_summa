# Instrucción: Un sistema de información cuenta con tres agentes (A, B y C) cada agente cumple con dos funcionalidades:
# Funcionalidad 1: Obtener media
# -	Definir la función getMedia(Lista de números reales) -> valor de retorno: número real
# -	Agente A: Obtener la media aritmética o promedio
# -	Agente B: Obtener media armónica
# -	Agente C: Obtener mediana
# Funcionalidad 2: Escalera
# -	Definir función getStaircase(número entero)  valor de retorno: cadena de texto
# -	Agente A: La base y altura son ambas iguales a n. Se dibuja usando el símbolo '#' símbolos y espacios. La última línea no va precedida de ningún espacio. 
# -	Agente B:
# La cima y altura son ambas iguales a n. Se dibuja usando el símbolo '#' símbolos y espacios. La primera línea no va precedida de ningún espacio
# -	Agente C:
# La base y cima son ambas iguales a n. Entre los extremos superior e inferior debe haber una distancia igual a n con el centro. Se dibuja usando el símbolo '#' símbolos y espacios

import statistics as stats
from typing import List

def get_media(lista_num_reales: List) -> float:
    """Get_media
    
    Args: Esta función recibe como argumento una lista de números reales

    Returns:
        Esta función retorna para el agente A: (float) la media aritmética o promedio.
        Para el agente B: (float) la media armónica.
        Para el agente C: (float) la mediana 
    """
    
    # Agente A: obtención de la media aritmetica
    media_aritmetica = stats.mean(lista_num_reales)
    print(f'Agente A: La media artimética de los datos ingresados es: {media_aritmetica:.2f}')
    
    # Agente B: obtención de la media armónica
    media_armonica = stats.harmonic_mean(lista_num_reales)
    print(f'Agente B: La media armónica de los datos ingresados es: {media_armonica:.2f}')
    
    # Agente C: obtención de la mediana
    mediana = stats.median(lista_num_reales)
    print(f'Agente C: La mediana de los datos ingresados es: {mediana:.2f}')
    
    return True

get_media([22, 23, 26, 26, 26, 34, 34, 38, 40])

def get_staircase(n:int):
    """Get_staircase
    
    Args: Esta función recibe como argumento un número entero

    Returns:
        Esta función retorna una cadena de texto (str) con las siguientes características:
        Para el agente A: escalera de tamaño n, donde n = argumento recibido
        Para el agente B: escalera invertida de tamaño n, donde n = argumento recibido
        Para el agente C: escalera de tamaño n con La base y cima iguales a n. Entre los extremos superior e inferior debe haber una distancia igual a n con el centro.
    """
    
    # Agente A: Escalera creciente de tamaño n
    print('Agente A:')
    for i in range (1,n+1):
        print(f'{"#" *i:>{n}}')
    print('-----------------------------')
    
    # Agente B: Escalera decreciente de tamaño n
    print('Agente B:')
    for j in range (n, 0, -1):
        print(f'{"#" *j:>{n}}')
    print('-----------------------------')
    
    # Agente C: Escalera con extremos superior e inferior iguales a n
    print('Agente C:')
    if n % 2 == 0:
        for i in range(n,2*n+2,2):
            print(f'{"#" *i:^{2*n+2}}')
        for i in range(2*n+2,n-1,-2):
            print(f'{"#" *i:^{2*n+2}}')
    else:
        for i in range(n,2*n+1,2):
            print(f'{"#" *i:^{2*n+1}}')
        for i in range(2*n+1,n-1,-2):
            print(f'{"#" *i:^{2*n+1}}')
    
    return True

#get_staircase(5)