import random
nmb = random.randint(0, 1000)
print('Numero random: ', nmb)
j = 0 # counter tentativi

while True:
    guess = int(input('Indovina l\'intero tra 0 e 1000: '))
    j += 1
    if guess == nmb:
        print(f'Indovinato in {j} tentativi!')
        break
    elif guess > nmb:
        print('Lower')
    else:
        print('Higher')