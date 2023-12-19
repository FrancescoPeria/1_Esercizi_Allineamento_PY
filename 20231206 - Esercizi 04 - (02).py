"""1) Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:
• Ask the user to input a word in English
• Make sure the user entered a valid word
• Convert the word from English to Pig Latin
• Display the translation result
Write and test a function that implements the a Pig Latin translator"""

def pig_latin_transator(stringa):
    # se iniziale della parola è >= 'A' ovvero il char con codifica ASCII più piccola
    # se finale della parola è <= 'z' ovvero il char con la codifica ASCII più grande
    if stringa[0] >= 'A' and  stringa[-1] <= 'z':
        return stringa[1:] + stringa[0] + 'ay'
    else:
        return 'Try Again!'



"""2) In the string "How much woot would a wootchuck chuck if a wootchuck could chuck the woot" the word
"wood" is misspelled. Use replace() to replace all occurrences of this spelling error with the correct spelling"""

def clean_mispellings(text):
    return text.replace('woot', 'wood')


""" 3) Write a program that prints a “cleaned” version of all the words in a string. Everything that is not a
letter should be removed and be considered a separator. All the letters should be lower case. For
example, the string "I'm sorry, sir." should produce four words, namely "i", "m", "sorry", and "sir" """

def clean_string(s):
    s = s.lower()
    temp = ''
    for j in s:
        if 'a' <= j <= 'z':
            temp += j
        else:
            temp += ' '
    list_split = temp.split(sep = ' ')
    risu = []
    for j in range(len(list_split)):
        if list_split[j] != '':
            risu.append(list_split[j])
    return risu


if __name__ == '__main__':

    # Test funzione 1)
    print('Test funzione 1)')
    while True:
        input_string = input('Inserisci una stringa in English: ')
        if pig_latin_transator != 'Try Again':
            print(pig_latin_transator(input_string))
            break


    # Test funzione 2)
    print('\nTest funzione 2)')
    text = "How much woot would a wootchuck chuck if a wootchuck could chuck the woot"
    print(clean_mispellings(text))


    #Test funzione 3)
    print('\nTest funzione 3)')
    text = "I'm sorry, sir."
    print(clean_string(text))


