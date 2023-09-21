# complejidad esperada: O(nlog(n))
# Dado un conjunto de puntos en un espacio bidimensional, tendr´as que encontrar la distancia
# euclideana entre los dos puntos m´as cercanos.
# Entrada
# La entrada contiene varios conjuntos de datos. Cada conjunto de datos comienza con un
# entero N (0 ≤ N ≤ 10000), que denota el n´umero de puntos en este conjunto. Las siguientes
# N l´ıneas contienen las coordenadas de N puntos bidimensionales. El primer n´umero denota
# la coordenada X y el segundo denota la coordenada Y . La entrada finaliza con un conjunto
# donde N = 0. El valor de las coordenadas ser´a menor que 40000 y no negativo.
# Salida
# Para cada conjunto de datos, produce una l´ınea de salida que contenga un n´umero de punto
# flotante (con cuatro d´ıgitos despu´es del punto decimal) que denote la distancia entre los dos
# puntos m´as cercanos. Si no existen dos puntos en la entrada cuya distancia sea menor que
# 10000, imprime la l´ınea ‘INFINITO’.

pruebas = []
caso = []
while True:
    try:
        entrada = input()
        if len(entrada.split(" ")) == 1:
            pruebas.append(caso)
            caso = []
        else:
            coordenadas = entrada.split(" ")
            caso.append((int(coordenadas[0]), int(coordenadas[1])))
    except Exception:
        break 
pruebas.remove([])