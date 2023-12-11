"""You roll five six-sided dice, one by one. How big is the probability that the
value of each die is greater than or equal to the value of the previous die that you rolled?
For example, the sequence “1, 1, 4, 4, 6” is a success, but “1, 1, 4, 3, 6” is not. Determine the
probability of success using a simulation of a large number of trials."""

import random
N_experiments = 1000000
M = 0 # Indicatore che mi dice quante volte la condizione vincente è falsa
N = 0 # Indicatore per il numero di esperimenti
while N < N_experiments:
    list_dice = []
    for j in range(5):
        list_dice.append(random.randint(1, 6))
        # a partire dal secondo dado tirato inizio il check per rilevare quando la condizione si invalida
        if j > 0 and (list_dice[j] < list_dice[j-1]):
            M += 1  # condizione vincente invalidata
            break # esco dal for perché ormai è invalidata
    print(list_dice)
    N += 1

print(f'Esperimenti totali: {N_experiments}',
      f'Esperimenti con successo: {N_experiments - M}',
      f'Probabilità di successo: {(N_experiments - M)/N_experiments}')