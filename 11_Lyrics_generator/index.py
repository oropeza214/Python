def mostrar_canciones(canciones):
    print("Por favor, selecciona una canción de la lista a continuación:\n")
    for indice, (titulo, artista) in enumerate(canciones, 1):
        print(f"{indice}. {titulo} por {artista}")
    print("\nPresiona * para elegir nuevamente.")
    print("Presiona / para salir.")

def main():
    canciones = [
        ("Baby", "Bieber"),
        ("Mommy", "Bieber"),
        ("Hotline Bling", "Drake"),
        ("Freeze Bling", "Drake"),
        ("Flawless", "Beyonce"),
        ("Flawplus", "Beyonce"),
        ("Fall", "Eminem"),
        ("Fly", "Eminem")
    ]

    letras = {
        "Baby": "Letras de muestra para Baby...",
        "Mommy": "Letras de muestra para Mommy...",
        "Hotline Bling": "Letras de muestra para Hotline Bling...",
        "Freeze Bling": "Letras de muestra para Freeze Bling...",
        "Flawless": "Letras de muestra para Flawless...",
        "Flawplus": "Letras de muestra para Flawplus...",
        "Fall": "Letras de muestra para Fall...",
        "Fly": "Letras de muestra para Fly..."
    }

    while True:
        artista = input("Ingresa el nombre del artista o presiona enter para ver todas las canciones: ").strip().title()
        if artista:
            canciones_filtradas = [(titulo, cantante) for titulo, cantante in canciones if cantante == artista]
        else:
            canciones_filtradas = canciones
        
        mostrar_canciones(canciones_filtradas)
        
        eleccion = input("\nTu elección: ")
        
        while eleccion != "*":
            if eleccion == "/":
                return
            elif eleccion.isdigit() and 0 < int(eleccion) <= len(canciones_filtradas):
                cancion_elegida = canciones_filtradas[int(eleccion)-1][0]
                print(f"\n------- {cancion_elegida} ------------")
                print(letras[cancion_elegida])
                print("\nPresiona * para elegir nuevamente o / para salir.")
            else:
                print("Elección inválida. Por favor, selecciona un número de canción válido.")
            
            eleccion = input("\nTu elección: ")

if __name__ == "__main__":
    main()
