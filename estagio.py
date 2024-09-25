def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def contar_letra_a(texto):
    return texto.lower().count('a')

def calcular_s(indice):
    s = 0
    k = 1
    while k < indice:
        k += 1
        s += k
    return s

# 1. Verificação se um número pertence à sequência de Fibonacci
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# 2. Contagem da letra 'a' em uma string
string = input("Informe uma string para contar a letra 'a': ")
quantidade = contar_letra_a(string)
print(f"A letra 'a' (ou 'A') aparece {quantidade} vezes na string.")

# 3. Cálculo da variável SOMA
indice = 12
s_resultado = calcular_s(indice)
print(f"A soma dos números de 1 até {indice - 1} é {s_resultado}.")
