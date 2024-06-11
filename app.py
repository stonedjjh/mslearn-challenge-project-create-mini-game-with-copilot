#leer por la consola un valor que solo puede ser de esta lista: ['rock', 'paper',  'scissors'] si la opcion no es valida debe solicitarse de nuevo la entrada debe ser convertida a minusculas
# si la opcion es valida se debe imprimir en consola la opcion elegida
# ejemplo de salida: usted selecciono rock
# ejemplo de salida: usted selecciono paper
# ejemplo de salida: usted selecciono 
#luego de seleccionar la opcion se debe seleccionar una opcion aleatoria de la lista ['rock', 'paper',  'scissors'] e imprimir en consola la opcion seleccionada
# ejemplo de salida: la computadora selecciono rock
# ejemplo de salida: la computadora selecciono paper
# ejemplo de salida: la computadora selecciono scissors
#rock > scissors
#scissors > paper
#paper > rock
#si el usuario gana se debe imprimir en consola "usted gana"
#si la computadora gana se debe imprimir en consola "usted pierde"
#si es un empate se debe imprimir en consola "empate"
#se debe llevar un contador de victorias, empates y derrotas
#al final del juego se debe imprimir en consola el numero de victorias, empates y derrotas
#se debe preguntar si se quiere volver a jugar
#si la respuesta es si se debe volver a jugar
#si la respuesta es no se debe terminar el juego
#se debe validar que la respuesta sea si o no
#ejemplo de salida: desea volver a jugar? si
#ejemplo de salida: desea volver a jugar? no
#ejemplo de salida: respuesta invalida
#se debe llevar un contador de juegos jugados
#al final del juego se debe imprimir en consola el numero de juegos jugados
#fin

import random

# Definir las opciones válidas y el mapa de victorias
opciones = ['rock', 'paper', 'scissors']
victorias = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

# Inicializar contadores
victorias_usuario = 0
victorias_computadora = 0
empates = 0
juegos_jugados = 0

# Función para jugar una ronda
def jugar():
    global victorias_usuario, victorias_computadora, empates
    opcion_usuario = input("Seleccione rock, paper o scissors: ").lower()
    while opcion_usuario not in opciones:
        print("Opción no válida. Intente de nuevo.")
        opcion_usuario = input("Seleccione rock, paper o scissors: ").lower()
    print(f"Usted seleccionó {opcion_usuario}")

    opcion_computadora = random.choice(opciones)
    print(f"La computadora seleccionó {opcion_computadora}")

    if opcion_usuario == opcion_computadora:
        print("Empate")
        empates += 1
    elif victorias[opcion_usuario] == opcion_computadora:
        print("Usted gana")
        victorias_usuario += 1
    else:
        print("Usted pierde")
        victorias_computadora += 1

# Bucle principal del juego
while True:
    jugar()
    juegos_jugados += 1

    seguir_jugando = input("¿Desea volver a jugar? (si/no): ").lower()
    while seguir_jugando not in ['si', 'no']:
        print("Respuesta inválida")
        seguir_jugando = input("¿Desea volver a jugar? (si/no): ").lower()

    if seguir_jugando == 'no':
        break

# Imprimir estadísticas finales
print(f"Juegos jugados: {juegos_jugados}")
print(f"Victorias: {victorias_usuario}, Empates: {empates}, Derrotas: {victorias_computadora}")


    


