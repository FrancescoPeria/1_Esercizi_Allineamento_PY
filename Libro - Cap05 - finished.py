"""5.1) Ask the user to enter a string. Then print the length of that string. Use the input()
function rather that the getString() function from , as the getString() function removes leading
and trailing spaces"""
s = input('Inserisci una stringa:')
print(len(s))

"""5.2) The Pythagorean theorem states that of a right triangle, the square of the
length of the diagonal side is equal to the sum of the squares of the lengths of the other two
sides (or a**2 + b**2 = c**2). Write a program that asks the user for the lengths of the two sides
that meet at a right angle, then calculate the length of the third side (in other words: take
the square root of the sum of the squares of the two sides that you asked for), and display
it in a nicely formatted way. You may ignore the fact that the user can enter negative or
zero lengths for the sides"""

a = float(input('Inserisci lato: '))
b = float(input('Inserisci lato: '))
c = (a**2 + b**2)**1/2
print(f'Cateto1: {a}\nCateto2: {b}\nCateto3: {c}')


"""5.3 Book) Ask the user to enter three numbers. Then print the largest, the
 smallest and their average rounded to 2 decimals. Fallo con l'if"""
def get_max(a, b, c):
    if a >= b and a >= c:
        risu = a
    if b >= a and b >= c:
        risu = b
    if c >= b and c >= a:
        risu = c
    return(risu)

def get_min(a, b, c):
    if a <= b and a <= c:
        risu = a
    if b <= a and b <= c:
        risu = b
    if c <= b and c <= a:
        risu = c
    return(risu)

N1 = float(input('Dammi un numero: '))
N2 = float(input('Dammi un numero: '))
N3 = float(input('Dammi un numero: '))

print('Minimo: {}\nMassimo: {}\nMedia: {}'.format(get_min(N1, N2, N3), get_max(N1, N2, N3), (N1 + N2 + N3)/3))


"""5.4) Calculate the value exp of to the power of -1, 0, 1, 2, and 3, and display the
results, with 5 decimals, in a nicely formatted manner."""

import math
print(f'Potenza -1: {math.exp(-1)}, Potenza 0: {math.exp(0)}, Potenza 1: {math.exp(1)}, Potenza 2: {math.exp(2)}, Potenza 3: {math.exp(-3)}')

"""5.5) Suppose you want to generate a random integer between 1 and 10 (1 and
10 both included), but from the random module you only have the random() function
available (you can use functions from other modules, though). How do you do that?"""
import random
rnd = int(random.random()*10) + 1
print(rnd)
