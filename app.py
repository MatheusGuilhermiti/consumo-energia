print("=== Calculadora de Consumo de Energia ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo = consumo_mensal * 0.75

print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f} por mês")