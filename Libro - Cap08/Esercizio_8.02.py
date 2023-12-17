"""Write a function that gets as parameters two strings. The function returns
the number of characters that the strings have in common. Each character counts only once,
e.g., the strings "bee" and "peer" only have one character in common (the letter “e”). You
can consider capitals different from lower case letters. Note: the function should return the
number of characters that the strings have in common, and not print it. To test the function,
you can print the result in your main program"""


def common_chars(stringa1, stringa2):
    N = 0  # Contatore numero di elementi in comune tra le due stringhe
    stringa_supporto = ''
    for j in stringa1:
        for k in stringa2:
            if j == k and j not in stringa_supporto:
                stringa_supporto += j
                N += 1
    return N, stringa_supporto


str1 = 'peeEr'
str2 = 'bEeeeee'
print(f'Elementi in comune:{common_chars(str1, str2)[1]}')
print(f'N°elementi in comune:{common_chars(str1, str2)[0]}')
