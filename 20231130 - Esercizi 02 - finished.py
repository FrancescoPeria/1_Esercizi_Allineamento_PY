
""" 1) Write a program that takes as input the length of the
sides of a rectangle and computes its perimeter and area """
l1 = 12
l2 = 5
perimeter = (l1 + l2)*2
A = l1*l2
print('Perimetro: {}\nArea: {}'.format(perimeter, A))

"""2) Write some code that asks the user for two numbers, 
then shows the result when you add them, and when you multiply them"""
a = input('Inserisci N1:')
b = input('Inserisci N2:')
a, b = int(a), int(b)
print('Somma: {}, Prodotto: {}'.format((a+b), (a*b)))


"""4) Create or download the pcinput module, make sure that it is located in the folder where you write your Python
code, then create a program that uses the functions described earlier"""

import pcinput

pcinput.getInteger('Dammi un int:')
pcinput.getFloat('Dammi un float:')
pcinput.getString('Dammi una string:')
pcinput.getLetter('Dammi una lettera alfabetica:')

"""3) Write ten times the string “I am writing ten times this string!”"""
print('I\'m writing ten times this string\n'*10)

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



""" 6.3 Book) Ask the user to supply a string. Print how many different vowels there
are in the string. The capital version of a lower case vowel is considered to be the same
vowel. y is not considered a vowel. Try to print nice output (e.g., printing “There are 1
different vowels in the string” is ugly). Example: When the user enters the string “It’s Owl
Stretching Time,” the program should say that there are 3 different vowels in the string."""

s = pcinput.getString('Inserisci una stringa:')
counter = 0
if ('a' in s) or ('A' in s):
    counter += 1
if ('e' in s) or ('E' in s):
    counter += 1
if ('i' in s) or ('I' in s):
    counter += 1
if ('o' in s) or ('O' in s):
    counter += 1
if ('u' in s) or ('U' in s):
    counter += 1
print('Numero di vocali: {}'.format(counter))

counter = 0
list_vocali = ['A', 'E', 'I', 'O', 'U']
for vocale in list_vocali:
    if vocale in s.upper():
        counter += 1
print('Numero di vocali: {}'.format(counter))



"""Given a sequence n integers (n from input), display the
sum and the mean of the numbers in the sequence that
are even, multiple of 3 and larger than the previous number"""


# MODO 1
list_input = [3, 9, 7, 12, 10, 24, 23, 45, 67, 21, 101, 44, 23]
cnt = 0
sum = 0
if (list_input[0]%2 == 0) and (list_input[0]%3 == 0):
    sum += list_input[0]
    cnt += 1
for j in range(1, len(list_input)):
    if (list_input[j]%2 == 0) and (list_input[j]%3 == 0) and (list_input[j] > list_input[j-1]):
        sum += list_input[j]
        cnt += 1
print('Somma numeri in lista: ', sum, 'Media numeri in lista: ', sum/cnt)

# MODO 2
prec = 0
sum = 0
cnt = 0
j = 0
n = int(input('Iserisci lunghezza lista:'))
while j < n:
    follow = int(input('Inserisci intero successivo'))
    if (follow % 2 == 0) and (follow % 3 == 0) and (follow > prec):
        sum += follow
        cnt += 1
    prec = follow
    j += 1
print('Somma numeri in lista: ', sum, 'Media numeri in lista: ', sum/cnt)