import pcinput
j = 0
LB = 0
UB = 1000
print(f'Indovinerò un int tra 0 e {UB}')
guess = int((UB - LB) / 2) # guess iniziale
j = 0 # counter tentativi

while True:

    if j > 10: # Se ci mette più di 10 mosse significa che ho imbrogliato con gli intervalli
        print('Hai imbrogliato con gli intervalli, non gioco più!')
        break

    feedback = pcinput.getLetter(f'Il numero che hai pensato è: {guess} ?' )

    if feedback == 'L':
        UB = guess
        guess = int((guess + LB) / 2)
        j += 1

    elif feedback == 'H':
        LB = guess
        guess = int((UB + guess) / 2)
        j += 1

    elif feedback == 'C':
        print(f'Indovinato in {j} tentativi')
        break

    else:
        print('Dammi una risposta corretta: H, L o C')
