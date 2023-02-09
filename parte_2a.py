# SOLUCIÓN DE LA FUNCIONALIDAD 1 SIN HACER USO DE LA LIBRERÍA ESTADÍSTICA 
from typing import List

def get_media(lista_num_reales: List):
    """Get_media
    
    Args: Esta función recibe como argumento una lista de números reales

    Returns:
        Esta función retorna para el agente A: (float) la media aritmética o promedio.
        Para el agente B: (float) la media armónica.
        Para el agente C: (float) la mediana 
    """
    
    # Agente A: obtención de la media aritmetica
    n = len(lista_num_reales)
    print(n)
    media_aritmetica = sum(lista_num_reales)/n
    print(f'Agente A: La media artimética de los datos ingresados es: {media_aritmetica:.2f}')
    
    # Agente B: obtención de la media armónica
    denominador = 0
    for i in lista_num_reales:
        denominador += (1/i)
        
    media_armonica = n/denominador
    print(f'Agente B: La media armónica de los datos ingresados es: {media_armonica:.2f}')
    
    # Agente C: obtención de la mediana
    # Ordena los datos de menor a mayor
    lista_num_reales.sort()
    
    # Cálculo de la mediana dependiendo si n es par o impar
    if n % 2 == 0:
        index1 = int(n/2)
        index2 = index1 - 1
        mediana = (lista_num_reales[index1] + lista_num_reales[index2])/2
        print(f'Agente C: La mediana de los datos ingresados es: {mediana:.2f}')
    else:
        index = round(n/2)-1
        mediana = lista_num_reales[index]
        print(f'Agente C: La mediana de los datos ingresados es: {mediana:.2f}')
    
    return True

#get_media([22, 23, 26, 26, 26, 34, 34, 38, 40])