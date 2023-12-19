"""Print a line of all the capital letters "A" to "Z". Below it, print a line of
the letters that are 13 positions in the alphabet away from the letters that are above them.
E.g., below the "A" you print an "N", below the "B" you print an "O", etcetera. You have to
consider the alphabet to be circular, i.e., after the "Z", it loops back to the "A" again"""

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))


j = 'A'
while j <= 'Z':
    print(j, ' ', end = '')
    j = chr(ord(j) + 1)

print(' ')

for i in range(26):
    nuova_posizione = (i + 13) % 26
    lettera = chr(ord('A') + nuova_posizione)
    print(lettera, ' ', end = '')