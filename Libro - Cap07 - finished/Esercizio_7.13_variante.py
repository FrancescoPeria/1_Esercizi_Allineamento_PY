"""You roll five six-sided dice, one by one. How big is the probability that the
value of each die is greater than or equal to the value of the previous die that you rolled?
For example, the sequence “1, 1, 4, 4, 6” is a success, but “1, 1, 4, 3, 6” is not. Determine the
probability of success using a simulation of a large number of trials."""

import random
N_experiments = 1000000
N = 0 # Indicatore per il numero di esperimenti
M = 0 # Indicatore che mi dice quante volte la condizione vincente è vera
cond = True # condizione di controllo
while N < N_experiments:
    dice_prec = 0
    for j in range(5):
        dice_succ = random.randint(1, 6)
        # a partire dal secondo dado tirato inizio il check per rilevare quando la condizione si invalida
        if dice_succ < dice_prec:
            cond = False
            break # esco dal for perché ormai è invalidata
        dice_prec = dice_succ
    if cond:
        M += 1

    N += 1

print(f'Esperimenti totali: {N_experiments}',
      f'Esperimenti con successo: {M}',
      f'Probabilità di successo: {M/N_experiments}')