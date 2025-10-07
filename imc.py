def imc(peso: float, altura: float) -> float:
    """Calcula o IMC (Índice de Massa Corporal)."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser positivos.")
    return round(peso / (altura ** 2), 2)
