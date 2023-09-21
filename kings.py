# complejidad esperada: O(nlog(n))
# En ocasi´on de la muerte del la reina Isabel II, la revista semanal
# estadounidense Times observ´o que el mayor n´umero de Reyes seleccionados en un per´ıodo de 100 a˜nos fue de 28, desde el a˜no 867
# (Felipo III) hasta el a˜no 975 (Mateo XIII) ,Hechos basados en la
# ficci´on. Esto es un dato muy interesante, pero ser´ıa mucho mejor
# contar con un programa para calcular ese n´umero para un per´ıodo
# de cualquier longitud, no necesariamente 100 a˜nos. Adem´as, dado
# que la instituci´on de la Monarqu´ıa es eterna, seg´un lo que podemos
# predecir, queremos asegurarnos de que nuestro programa siga siendo
# v´alido per omnia secula seculorum.
# Escribe un programa que, dado una lista de a˜nos en los que cada Reina/Rey fue coronado y
# un n´umero positivo Y , calcule el mayor n´umero de Reyes que estuvieron en el trono en un
# per´ıodo de Y a˜nos, as´ı como el a˜no de coronaci´on del primer y ´ultimo Rey en ese per´ıodo. Ten
# en cuenta que, dado un a˜no N, el per´ıodo de Y a˜nos que comienza en el a˜no N es el intervalo
# de tiempo que va desde el primer d´ıa del a˜no N hasta el ´ultimo d´ıa del a˜no N + Y − 1. En
# caso de empate, es decir, si existen varios per´ıodos de Y a˜nos con el mismo mayor n´umero de
# Reyes, tu programa debe reportar solo el m´as antiguo.
# Entrada
# La entrada contendr´a varios casos de prueba, cada uno de ellos como se describe a continuaci´on. Los casos de prueba consecutivos est´an separados por una sola l´ınea en blanco. La
# primera l´ınea de la entrada contiene un n´umero entero positivo Y , el n´umero de a˜nos del
# per´ıodo que nos interesa. La segunda l´ınea contiene otro n´umero entero positivo, el n´umero
# de Reyes, R. Cada una de las R l´ıneas siguientes contiene el a˜no de coronaci´on de un Rey, en
# orden cronol´ogico.
# Salida
# Para cada caso de prueba, escribe en la salida una sola l´ınea con tres n´umeros enteros,
# separados por espacios: el mayor n´umero de Reyes en un per´ıodo de Y a˜nos, el a˜no de
# coronaci´on  del primer Rey en ese per´ıodo y el a˜no de coronaci´on del ´ultimo Rey en ese
# per´ıodo.


pruebas = []
linea = 0
caso = {}
while True:
    try:
        entrada = input()
        if entrada == "":
            linea = 0
            pruebas.append(caso)
            caso = {}
        else:
            if linea == 0:
                caso['periodo'] = int(entrada)
                caso['anios'] = []
                linea += 1
            elif linea == 1:
                linea += 1
            elif linea == 2:
                caso['anios'].append(int(entrada))
    except Exception:
        break 

def kings_interseccion(periodo, lista):

    mitad = len(lista)//2
    lista_izquierda = lista[:mitad]
    lista_derecha = lista[mitad:]

    if lista_derecha[0] - lista_izquierda[len(lista_izquierda)-1] - 1 >  periodo:
        return 0, 0, 0

    else:

        lista_izquierda_apuntador = len(lista_izquierda)-1
        lista_derecha_apuntador = 0
        interseccion_maximoreyes = 2


        for i in range(len(lista)):
            if (lista_derecha_apuntador+1 < len(lista_derecha)) and (lista_derecha[lista_derecha_apuntador+1] - lista_izquierda[lista_izquierda_apuntador] - 1 <=  periodo):
                lista_derecha_apuntador += 1
                interseccion_maximoreyes += 1
            elif (lista_izquierda_apuntador-1 >= 0) and (lista_derecha[lista_derecha_apuntador] - lista_izquierda[lista_izquierda_apuntador-1] - 1 <=  periodo):
                lista_izquierda_apuntador -= 1
                interseccion_maximoreyes += 1
        
        return interseccion_maximoreyes, lista_izquierda[lista_izquierda_apuntador], lista_derecha[lista_derecha_apuntador]
    
def kings(periodo: int, lista:list[int]) -> tuple:

    if len(lista) == 1:
     return 1, lista[0], lista[0]
    else: 
        medio = len(lista) // 2
        lista_izquierda = lista[:medio]
        lista_derecha = lista[medio:]

        izquierda_maximoreyes, izquierda_primeranio, izquierda_segundoanio = kings(periodo, lista_izquierda)
        derecha_maximoreyes, derecha_primeranio, derecha_segundoanio = kings(periodo, lista_derecha)
        interseccion_maximoreyes, interseccion_primeranio, interseccion_segundoanio = kings_interseccion(periodo, lista)
        
        maximoreyes_maximo = max(izquierda_maximoreyes, derecha_maximoreyes, interseccion_maximoreyes)
        #print(lista_izquierda)
        #print(lista_derecha)
        if izquierda_maximoreyes == maximoreyes_maximo:
            #print(izquierda_maximoreyes, izquierda_primeranio, izquierda_segundoanio)
            return (izquierda_maximoreyes, izquierda_primeranio, izquierda_segundoanio)
        elif interseccion_maximoreyes == maximoreyes_maximo:
            #print(interseccion_maximoreyes, interseccion_primeranio, interseccion_segundoanio)
            return (interseccion_maximoreyes, interseccion_primeranio, interseccion_segundoanio)
        elif derecha_maximoreyes == maximoreyes_maximo:
            #print(derecha_maximoreyes, derecha_primeranio, derecha_segundoanio)
            return (derecha_maximoreyes, derecha_primeranio, derecha_segundoanio)
    
for i in range(len(pruebas)):    
    print(kings(pruebas[i]['periodo'], pruebas[i]['anios']))