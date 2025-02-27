"""
Programa: ex10_investimento
Descrição: Este programa calcula o valor capitalizado em um investimento de juros composto à taxas constantes.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória

capital = 0
prazo = 0
taxa = 0

# Entrada de dados 

capital = float(input("Qual o valor que será investido, em reais?"))
prazo = int(input("Qual o prazo do investimento, em meses?"))
taxa = float(input("Qual a taxa mensal do investimento? Insira o valor sem %"))

# Processamento de dados 

montante = capital*(1+taxa/100)**prazo

# Saída de dados 
print(f"Seu montante após {prazo} meses, será de {montante: .2f}")