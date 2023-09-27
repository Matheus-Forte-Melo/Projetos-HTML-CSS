somas = []
lista = [2, 3, 3, 5, 2, 5 , 1, 4]
target = 6


def descobreSoma(nums, target):
    hashMap = {}

    for pos, i in enumerate(nums):
        hashMap[pos] = i
        
    for pos, item in hashMap.items():
        complemento = target - item
        if complemento in hashMap and (item, complemento) not in somas and (complemento, item) not in somas:
            somas.append((item, complemento))
    return somas

lista = []
contador = 0
while True:
    contador += 1
    valor = int(input(f"[999 para parar] {contador}° valor: "))

    if valor == 999 and contador <= 2:
        print("ATENÇÃO: Insira pelo menos dois números!")
        contador -= 1
        continue
    elif valor == 999:
        break

    lista.append(valor)
    print(lista)
    
target = int(input("Valor de soma que você quer encontrar na lista: "))
resultado = descobreSoma(lista, target)

print("Para alcançar 6 com dois números some:")

for tupla in resultado:
    if tupla[0] > tupla[1]:
        print(f"{tupla[0]} + {tupla[1]}", end=" | ")
    else:
        print(f"{tupla[1]} + {tupla[0]}", end=" | ")