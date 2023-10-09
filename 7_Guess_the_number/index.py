import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Adivina un número entre 1 y 50: "))
            intentos += 1

            if 1 <= adivinanza <= 50:
                if adivinanza < numero_secreto:
                    print("Intenta con un número más grande.")
                elif adivinanza > numero_secreto:
                    print("Intenta con un número más pequeño.")
                else:
                    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                    break
            else:
                print("Por favor, elige un número dentro del rango del 1 al 50.")
                
        except ValueError:
            print("Por favor, introduce un número válido.")

        continuar = input("¿Quieres seguir jugando? (sí/no): ").lower()
        if continuar == 'no':
            print(f"El número secreto era {numero_secreto}. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    jugar_adivina_el_numero()
