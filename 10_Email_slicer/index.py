def descomponer_email(email: str) -> tuple:
    """Descompone el email en usuario y dominio."""
    partes = email.split('@')
    usuario = partes[0]
    dominio = partes[1]
    return usuario, dominio

def identificar_dominio(dominio: str) -> str:
    """Identifica si el dominio es popular o personalizado."""
    dominios_populares = {
        "gmail.com": "Google",
        "yahoo.com": "Yahoo",
        "outlook.com": "Outlook",
        "hotmail.com": "Hotmail"
    }
    return dominios_populares.get(dominio, "")

def main():
    email = input("Por favor, introduce tu dirección de email: ")
    usuario, dominio = descomponer_email(email)
    nombre_usuario = usuario.split('.')[0].capitalize()

    dominio_identificado = identificar_dominio(dominio)

    if dominio_identificado:
        print(f"¡Hola {nombre_usuario}! Veo que tu email está registrado con {dominio_identificado}. ¡Eso es genial!")
    else:
        nombre_dominio = dominio.split('.')[0].capitalize()
        print(f"¡Hola {nombre_usuario}! Parece que tienes tu propia configuración personalizada en {nombre_dominio}. ¡Impresionante!")

if __name__ == "__main__":
    main()
