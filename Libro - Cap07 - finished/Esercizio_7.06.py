"""Write a program that asks the user for two words. Then print all the characters that the words have in common.
You can consider capitals different from lower case letters, but each character that you report,
should be reported only once (e.g., the strings “bee” and “peer” only have one character in common,
namely the letter “e”). Hint: Gather the characters in a third string, and when you find a
character that the two words have in common, check if it is already in the third string before reporting it"""

stringa1 = input('Inserisci una stringa: ')
stringa2 = input('Inserisci una stringa: ')
stringa3 = ''

for j in stringa1:
    for k in stringa2:
        if (j == k) and (j not in stringa3):
            stringa3 = stringa3 + j
print('Lettere che stringa1 e stringa2 hanno in comune: ', stringa3)