"""1) Write code that for a string prints the indices of all of its vowels (a, e,
i, o, and u). This can be done with a for loop or a while loop, though
the while loop is more suitable"""

def get_vowels_idx(s):
    j = 0
    vowels_idx = []
    while j < len(s):
        if s[j] in 'aeiouAEIOU':
            vowels_idx.append(j)
        j += 1
    return vowels_idx


"""2) Write code that uses two strings. For each character in the first string
that has exactly the same character at the same index in the second
string, you print the character and the index. Watch out that you do
not get an “index out of bounds” runtime error. Test it with the strings
"The Holy Grail" and "Life of Brian"""

def get_commom_chars(str1, str2):
    dict_common_chars = {}
    j = 0
    # Il vincolo di lunghezza ce l'ha str1
    if len(str1) <= len(str2):
        while j < len(str1):
            if str1[j] == str2[j]:
                dict_common_chars[j] = str1[j]
            j += 1
    else:
        while j < len(str2):
            if str2[j] == str1[j]:
                dict_common_chars[j] = str2[j]
            j += 1
    return dict_common_chars


"""3) Write a function that takes a string as argument, and creates a new
string that is a copy of the argument, except that every non-letter is
replaced by a space (e.g., "ph@t l00t" is changed to "ph t l t"). To
write such a function, you will start with an empty string, and traverse
the characters of the argument one by one. When you encounter a
character that is acceptable, you add it to the new string. When it is
not acceptable, you add a space to the new string. Note that you can
check whether a character is acceptable by simple comparisons. For
example, any lower case letter can be found using the test if >= 'a' and <= ‘z':"""

def spacy_string(str):
    temp = ''
    for j in str:
        if ('a' <= j <= 'z') or ('A' <= j <= 'Z'):
            temp += j
        else:
            temp += ' '
    return temp



def main():
    print('1) Esercizio sulle vocali')
    stringa = input('Inserisci una stringa: ')
    print('Idx delle vocali nella stringa inserita: ', get_vowels_idx(stringa))
    print('\n', 60*'*', '\n')

    print('2) Esercizio sulle lettere in comune tra due stringhe')
    stringa1 = input('Inserisci stringa1: ')
    stringa2 = input('Inserisci stringa2: ')
    print('Associazione indice comunanze e valori a comune', get_commom_chars(stringa1, stringa2))
    print('\n', 60 * '*', '\n')

    print('3) Esercizio sui caratteri speciali rimpiazzati da spazi')
    stringa = input('Inserisci stringa: ')
    print('Stringa senza le non-lettere', spacy_string(stringa))
    print('\n', 60 * '*', '\n')


if __name__ == '__main__':
    main()
