# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
numero = []
for inserir in range(10):
     Numero = int(input("Digite número: "))
     if Numero % 2 == 0:
           numero.append(Numero)
soma = sum(numero)
print(soma)