#  complejidad esperada: O(nlog(n)).
# Imagina que eres un valiente superviviente tratando de atravesar
# un mundo postapocal´ıptico al estilo de Mad Max. Muchos peligros
# y obst´aculos esperan en tu camino. Tu vida depende de tu leal
# y antiguo veh´ıculo todoterreno, el cual debe contar con un tanque
# de combustible lo suficientemente grande. Pero, ¿exactamente cu´an
# grande debe ser? Calcula el volumen m´as peque˜no necesario para
# alcanzar tu objetivo (El Valhalla) .
# Los siguientes eventos describen tu traves´ıa:
# • Consumo de combustible n: indica que tu veh´ıculo necesita n litros de gasolina por cada
# 100 km.El consumo de combustible puede cambiar durante tu viaje, por ejemplo, cuando
# conduces cuesta arriba o cuesta abajo de una monta˜na.
# • Disparo enemigo: significa que tu veh´ıculo fue alcanzado por un disparo enemigo. El
# tanque comenzar´a a perder gasolina a una velocidad de 1 litro de combustible por cada
# kil´ometro. Los disparos enemigos m´ultiples se suman y hacen que el veh´ıculo pierda
# combustible a un ritmo m´as r´apido.
# • Repostaje en Oasis: te permite llenar tu tanque en un oasis en medio del desierto, un
# refugio donde los valientes sobrevivientes pueden abastecerse de recursos.
# • Tuneo en la Guarida: realiza mejoras cruciales en tu veh´ıculo en una guarida oculta en
# el desierto, donde los maestros artesanos mejoran tu tanque y te dan una oportunidad
# real de ´exito.
# • Valhalla: significa que has llegado con seguridad a la legendaria Tierra Prometida, un
# lugar donde los valientes obtienen su merecido descanso.
# • Los Oasis y las guaridas cumplen funciones independientes es decir en los Oasis no
# reparar y en las guaridas no se puede llenar el tanque
# Entrada
# La entrada consiste en una serie de casos de prueba. Cada evento est´a descrito por un n´umero
# entero, la distancia (en kil´ometros desde el inicio) en la que ocurre el evento, seguido por el
# tipo de evento mencionado anteriormente.
# En cada caso de prueba, el primer evento tiene la forma ‘0 consumo de combustible n’, y
# el ´ultimo evento tiene la forma ‘d Valhalla’ (d es la distancia a la Tierra Prometida). Los
# eventos est´an ordenados seg´un la distancia desde el inicio, y el evento ‘d Valhalla’ siempre es
# el ´ultimo. Puede haber varios eventos en la misma distancia; procesales en el orden dado.
# La entrada finaliza con una l´ınea que contiene ‘0 consumo de combustible 0’, que no debe
# procesarse.
# Salida
# Para cada caso de prueba, imprime una l´ınea que contenga el volumen de tanque m´as peque˜no
# posible (en litros, con tres d´ıgitos de precisi´on despu´es del punto decimal) que garantice una
# traves´ıa exitosa hacia la Tierra Prometida.