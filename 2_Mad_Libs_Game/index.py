def main():
    # Solicitar al usuario diversas entradas
    name = input("Por favor, ingresa un nombre: ")
    adjective = input("Ahora, ingresa un adjetivo: ")
    pronoun = input("Ingresa un pronombre (él/ella/usted): ")
    action = input("Finalmente, ingresa una acción (ejemplo: 'correr'): ")

    # Crear la historia con las palabras dadas
    story = f"Un día, {name} estaba caminando por el parque cuando, de repente, se sintió {adjective}. {pronoun.capitalize()} decidió {action} hacia la salida más cercana."

    # Imprimir la historia
    print("\n¡Aquí está tu historia!")
    print(story)

if __name__ == "__main__":
    main()
