def calcular_propina(total: float, porcentaje: float) -> float:
    """Calcula la propina basada en el total y el porcentaje."""
    return round(total * porcentaje, 2)

def main():
    total = float(input("¿Cuál es el total de la cuenta para hoy, por favor?: $"))

    for porcentaje in [0.18, 0.20, 0.25]:
        propina = calcular_propina(total, porcentaje)
        total_con_propina = total + propina
        print(f"La propina del {int(porcentaje*100)}% es ${propina:.2f}, lo que hace un total de ${total_con_propina:.2f}")

    personas = int(input("\n¿Cuántas personas están involucradas?: "))
    if personas > 1:
        porcentaje_individual = float(input("Por favor, ingresa el porcentaje que cada persona cubrirá (ejemplo: 50 para 50%): ")) / 100
        parte_individual = total_con_propina * porcentaje_individual
        print(f"Cada persona deberá pagar: ${parte_individual:.2f}")

if __name__ == "__main__":
    main()
