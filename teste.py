lista = [3,3,7,1,6, 6]
target = 6

def descobreSoma(nums, target):
    hashMap = {}

    for pos, num in enumerate(nums):
        hashMap[num] = pos 
        print(hashMap)

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashMap and hashMap[complement] != i: # Ele procura pela key
            return (i, hashMap[complement])
        return []
        

        
    

print(descobreSoma(lista, target))