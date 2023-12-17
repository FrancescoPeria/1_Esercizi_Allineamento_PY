nmb = int(input('Inserisci un intero: '))
cnt = 0
for j in range(1, nmb): # non ci arrivo mai a dividere il numero per sé stesso
    if nmb % j == 0:
        cnt += 1
    if cnt > 1: # se il numero è divisibile per altri numeri al di fuori di 1
        print('Il numero non è primo')
        break
else:
    print('Il numero è primo')
