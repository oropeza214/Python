def obtener_acronimo(frase: str) -> str:
    palabras = [palabra for palabra in frase.split() if len(palabra) > 2]  # Filtrar palabras con 2 letras o menos
    acronimo = [palabra[0].upper() for palabra in palabras]
    return ''.join(acronimo)

def main():
    frase = input("Introduce el nombre completo de una organización o concepto: ")
    acronimo = obtener_acronimo(frase)
    print(f"El acrónimo de '{frase}' es: {acronimo}")

if __name__ == "__main__":
    main()
