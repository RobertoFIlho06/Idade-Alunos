id_max = int(input("Qual é a idade máxima dos alunos?: "))

while id_max <= 0:
    print("A idade não pode ser menor que 0")
    id_max = int(input("digite novamente."))

qtd_id = int(input("Quantas idades devem ser apresentados?: "))

while qtd_id <= 0:
    print("A Idade não pode ser menor que 0")
    qtd_id = int(input("digite novamente."))

p_i = input("Quer que sejam apresentadas idades pares ou ímpares?")
contador = 0

for n in range(1, id_max + 1):

    if p_i == "pares" and n % 2 == 0:
        print(n)
        contador += 1
    elif (p_i == "ímpares" or p_i == "impares") and n % 2 == 1:
        print(n)
        contador += 1

    if contador == qtd_id:
        break


