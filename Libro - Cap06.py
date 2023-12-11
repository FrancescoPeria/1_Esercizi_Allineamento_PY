"""6.1) Grades are values between zero and 10 (both zero and 10 included), and
are always rounded to the nearest half point. To translate grades to the American style, 8.5
to 10 become an “A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become
a “D,” and other grades become an “F.” Implement this translation, whereby you ask the
user for a grade, and then give the American translation. If the user enters a grade lower
than zero or higher than 10, just give an error message. You do not need to handle the user
entering grades that do not end in .0 or .5, though you may do that if you like – in that case,
if the user enters such an illegal grade, give an appropriate error message."""

grade = float(input('Inserisci voto: '))
if grade < 0 or grade > 10 or grade % 0.5 != 0:
    print('Inserisci una stringa a modo')
else:
    if grade >= 8.5 and grade <= 10:
        american_grade = 'A'
    elif grade >= 7.5 and grade <= 8:
        american_grade = 'B'
    elif grade >= 6.5 and grade <= 7:
        american_grade = 'C'
    elif grade > 5.5 and grade <= 6:
        american_grade = 'D'
    else:
        american_grade = 'F'
    print(f'Voto italiano: {grade}, Voto americano: {american_grade}')


""" 6.3 Book) Ask the user to supply a string. Print how many different vowels there
are in the string. The capital version of a lower case vowel is considered to be the same
vowel. y is not considered a vowel. Try to print nice output (e.g., printing “There are 1
different vowels in the string” is ugly). Example: When the user enters the string “It’s Owl
Stretching Time,” the program should say that there are 3 different vowels in the string."""
import pcinput
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


"""6.4) Descrizione troppo lunga"""

A = int(input('Inserisci A: '))
B = int(input('Inserisci B: '))
C = int(input('Inserisci C: '))

delta = B**2 - 4*A*C

if (B == A == 0 and C != 0) or delta < 0:
    print('Impossibile')
elif delta == 0:
    sol = -B / (2*A)
    print(f'Esiste una soluzione{sol}')
else:
    sol1 = (-B + (B**2 - 4*A*C)**0.5 )/(2*A)
    sol2 = (-B - (B**2 - 4*A*C)**0.5 )/(2*A)
    print(f'Esistono 2 soluzioni: {sol1} ; {sol2}')




