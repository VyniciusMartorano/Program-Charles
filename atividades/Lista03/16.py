"""
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor corresponde ao valor de
um saque em um terminal de caixa eletrônico) e que calcule a quantidade de cédulas de R$ 100,00, R$
50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$
0,05 e R$ 0,01. 
"""
#round é pra arredondar pra baixo

valor = 146

valorParcial = valor

if valorParcial >= 100:
    notasDeCem = (valorParcial / 100)
    print(f'{notasDeCem} Nota(s) de R$100.')
    valorParcial -= (notasDeCem * 100)

if valorParcial >= 50:
    notasDeCinquenta = round(valorParcial / 50)
    print(f'{notasDeCinquenta} Nota(s) de R$50.')
    valorParcial -= (notasDeCinquenta * 50)

if valorParcial >= 10:
    notasDeDez = round(valorParcial / 10)
    print(f'{notasDeDez} Nota(s) de R$10.')
    valorParcial -= (notasDeDez * 10)

if valorParcial >= 5:
    notasDeCinco = round(valorParcial / 5)
    print(f'{notasDeCinco} Nota(s) de R$5.')
    valorParcial -= (notasDeCinco * 5)

if valorParcial >= 1:
    notasDeUm = round(valorParcial / 1)
    print(f'{notasDeUm} Nota(s) de R$1.')
    valorParcial -= (notasDeUm * 1)
