""" The text below, count how often the word “wood” occurs (using program code, of course).
Capitals and lower case letters may both be used, and you have to
consider that the word “wood” should be a separate word, and not part of another word.
Hint: If you did the exercises from this chapter, you already developed a function that
“cleans” a text. Combining that function with the split() function more or less solves the
problem for you."""


text = """How much wood would a woodchuck chuck If a woodchuck could chuck wood?
He would chuck , he would , as much as he could , And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def cleans(testo):
    testo = testo.lower() #metto tutto in lower case
    temp = ''
    for carattere in testo:
        if 'a' <= carattere <= 'z':
            temp += carattere
        else:
            temp += ' '
    return temp

text_cleaned = cleans(text)
list_text = text_cleaned.split(sep = ' ')
print(list_text)

cnt = 0
for j in list_text:
    if j == 'wood':
        cnt += 1
print('Il numero di occorrenze di wood è: ', cnt)
