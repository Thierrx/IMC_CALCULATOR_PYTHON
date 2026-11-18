def calcular_imc(peso, altura):
    """Calcula o IMC depois de validar peso e altura."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")

    return peso / (altura ** 2)


def classificar_imc(imc):
    """Retorna a faixa correspondente ao IMC informado."""
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso ideal"
    if imc < 30:
        return "Sobrepeso"
    if imc < 35:
        return "Obesidade grau 1"
    if imc < 40:
        return "Obesidade grau 2"
    return "Obesidade grau 3"
