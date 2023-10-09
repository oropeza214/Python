def es_palindromo(palabra: str) -> bool:
    """Revisa si una palabra es un palíndromo."""
    return palabra == palabra[::-1]

def main():
    palabras = []

    for i in range(5):
        palabra = input(f"Introduce la palabra #{i + 1}: ").strip().lower()
        palabras.append(palabra)

    for palabra in palabras:
        if es_palindromo(palabra):
            print(f"'{palabra}' es un palíndromo.")
        else:
            print(f"'{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()