def obtener_input(mensaje: str) -> str:
    while True:
        respuesta = input(mensaje)
        if respuesta.strip() == "":
            print("La entrada no es válida. Intenta de nuevo.")
        else:
            return respuesta

def main():
    print("Por favor, introduce tu información personal.")
    
    # Solicitar información al usuario
    nombre = obtener_input("¿Cuál es tu nombre? ")
    fecha_nacimiento = obtener_input("¿Cuál es tu fecha de nacimiento? (Ejemplo: 1 de Enero, 2000) ")
    direccion = obtener_input("¿Cuál es tu dirección? (Ejemplo: Av. Siempre Viva 123, Springfield) ")
    metas_personales = obtener_input("¿Cuáles son tus metas personales? ")

    # Mostrar un resumen de la información
    print("\nResumen de tu Información:")
    print(f"- Nombre: {nombre}")
    print(f"- Fecha de nacimiento: {fecha_nacimiento}")
    print(f"- Dirección: {direccion}")
    print(f"- Metas personales: {metas_personales}")

if __name__ == "__main__":
    main()
