def descobreSoma(nums, target):
    hashMap = {}

    for pos, i in enumerate(nums):
        hashMap[i] = pos

    for pos, i in enumerate(nums):
        complement = target - i
        if complement in hashMap and pos != hashMap[complement]:
            return (pos, hashMap[complement])
    return []
            

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
print(lista)
print(descobreSoma(lista, target))



