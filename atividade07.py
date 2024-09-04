# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

valorproduto = int(input("Digite o valor do seu produto "))

calcimposto = (valorproduto * 12) /100
valorcomimposto = calcimposto + valorproduto

print("Seu valor final é: ", valorcomimposto)