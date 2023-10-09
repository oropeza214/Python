import random

def eleccion_jugador():
    """Obtiene la elección del jugador."""
    print("Elige: piedra, papel o tijera.")
    eleccion = input().lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        print("Entrada no válida. Elige: piedra, papel o tijera.")
        eleccion = input().lower()
    return eleccion

def eleccion_computadora():
    """Obtiene una elección aleatoria para la computadora."""
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(jugador, computadora):
    """Determina el ganador del juego."""
    if jugador == computadora:
        return 'empate'
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        return 'jugador'
    else:
        return 'computadora'

def main():
    jugador = eleccion_jugador()
    computadora = eleccion_computadora()
    
    print(f"\nJugador eligió: {jugador}")
    print(f"Computadora eligió: {computadora}")

    resultado = determinar_ganador(jugador, computadora)

    if resultado == 'empate':
        print("¡Es un empate!")
    elif resultado == 'jugador':
        print("¡Felicidades, ganaste!")
    else:
        print("La computadora ganó. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    main()
