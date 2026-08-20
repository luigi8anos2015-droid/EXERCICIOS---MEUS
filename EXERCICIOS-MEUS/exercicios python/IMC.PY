def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser maiores que zero."
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return f"IMC: {imc:.2f} ({categoria})"

# Exemplo de uso
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
print(calcular_imc(peso, altura))