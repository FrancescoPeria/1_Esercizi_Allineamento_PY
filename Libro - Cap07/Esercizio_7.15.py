"""According to an old puzzle, five pirates and their monkey are stranded on
an island. During the day they gather coconuts, which they put in a big pile. When night
falls, they go asleep.
In the middle of the night, the first pirate wakes up, and, not trusting his buddies, he
divides the pile into five equal parts, takes what he believes to be his share and hides it.
Since he had one coconut left after the division, he gives it to the monkey. Then he goes
back to sleep.
An hour later, the next pirate wakes up. He behaves in the same way as the first pirate:
he divides the pile into five equal shares, with one coconut left over which he gives to the
monkey, hides what he believes to be his share, and goes to sleep again.
The same happens to the other pirates: they wake up one by one, divide the pile, give one
coconut to the monkey, hide their share, and go back to sleep.
In the morning they all wake up. They divide what remains of the coconuts equally
amongst them. Since that leaves one coconut, they give it to the monkey.
The question is: what is the smallest number of coconuts that they can have started with?
Write a Python program that solves this puzzle. If you can solve it for any number of
pirates, all the better"""

N_pirati = 5
qty = N_pirati + 1

while True:
    solved = True
    temp = qty
    print(f'Noci di cocco: {qty}')
    for p in range(N_pirati+1):
        qty_scimmia = temp % N_pirati
        qty_pirata = int(temp / N_pirati)
        print(f'Scimmia: {qty_scimmia}')
        print(f'Pirata: {qty_pirata}')
        if qty_scimmia == 1:
            temp = temp - qty_pirata - qty_scimmia
        else:
            solved = False
            break
    print('')
    if solved:
        print(f'La minima quantità di noci che risolve il puzzle è {qty}')
        break
    qty += 1
