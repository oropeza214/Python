def main():
    # Dar la bienvenida al usuario
    print("¡Bienvenido!")

    # Pedir al usuario un número entre 1 y 1000
    number = int(input("Por favor, ingresa un número entre 1 y 1000: "))

    # Comprobar si el número está en el rango deseado
    if 1 <= number <= 1000:
        # Determinar si el número es par o impar
        if number % 2 == 0:
            print("El número que ingresaste es par.")
        else:
            print("El número que ingresaste es impar.")
    else:
        print("Por favor, asegúrate de ingresar un número en el rango indicado.")

if __name__ == "__main__":
    main()
