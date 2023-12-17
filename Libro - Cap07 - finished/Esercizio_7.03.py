"""Write a program that asks the user for ten numbers, and then prints the
largest, the smallest, and how many are divisible by 3. Use the algorithm described earlier
in this chapter"""

nmb = input('Inserisci un numero: ') # Inizializzo fuori dal while per gestire max_nmb e min_nmb
nmb = float(nmb)
cnt = 0 # counter per i multipli di 3
max_nmb = nmb
min_nmb = nmb
j = 1
while j < 10:
    nmb = input('Inserisci un numero: ')
    nmb = float(nmb)
    if nmb > max_nmb:
        max_nmb = nmb
    if nmb < min_nmb:
        min_nmb = nmb
    if  nmb % 3 == 0:
        cnt += 1
    j+=1
print(f'Max: {max_nmb}\nMin: {min_nmb}\nQuanti numeri divisibili per 3:{cnt}')



"""Altro modo con continue"""

cnt = 0 # counter per i multipli di 3
j = 0
while j < 10:
    nmb = input('Inserisci un numero: ')
    nmb = float(nmb)
    if j == 0: # gestire l'inizializzazione di max_nmb e min_nmb nel ciclo while
        max_nmb = nmb
        min_nmb = nmb
        j+=1
        continue
    if nmb > max_nmb:
        max_nmb = nmb
    if nmb < min_nmb:
        min_nmb = nmb
    if  nmb % 3 == 0:
        cnt += 1
    j+=1

print(f'Max: {max_nmb}\nMin: {min_nmb}\nQuanti numeri divisibili per 3:{cnt}')