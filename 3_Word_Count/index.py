def main():
    # Preguntar al usuario qué piensa
    frase = input("¿Qué tienes en mente hoy? ")

    # Contar el número de palabras en la respuesta
    conteo_palabras = len(frase.split())

    # Imprimir el resultado
    print(f"Vaya, ¡acabas de compartir lo que piensas en {conteo_palabras} palabras!")

if __name__ == "__main__":
    main()
