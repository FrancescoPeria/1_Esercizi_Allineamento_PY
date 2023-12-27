"""1) Write a program that reads an integer number n, creates
a list that contains the first n positive integers, and prints it"""

N = int(input('Inserisci un numero: '))
lista = []
j = 1
while j <= N:
    lista.append(j)
    j += 1
print(lista)


""" 3) Write a program that reads from input a list of n integers and displays the sum, 
      the mean, the max and the min only of the even numbers in the list """

def create_list(n):
    j = 0
    list_number = []
    while j < n:
        number = int(input('Inserisci intero: '))
        list_number.append(number)
        j += 1
    return list_number

def get_stats(n):
    l = create_list(n)
    temp = []
    for j in l:
        if j % 2 == 0:
            temp.append(j)
    return sum(temp), sum(temp)/len(temp), max(temp), min(temp)

print(get_stats(10))



"""Write a program that reads from input a list of n integers and displays the sum and the mean of the numbers in
the list that are even, divisible by 3 and greater than the previous one (assume the conditions to be true for the
first element) """

N = 5
j = 0
list_nmb = []
sum = 0
cnt = 0
previous = 0
while j < N:
    nmb = int(input('Inserisci numero: '))
    list_nmb.append(nmb)
    if (nmb % 2 == 0) and (nmb % 3 == 0) and (nmb > previous):
        cnt += 1
        sum += nmb
    previous = nmb
    j += 1

if cnt > 0:
    print('Average of numbers: ', sum / cnt)
    print('Sum of numbers:', sum)
else:
    print('No data satisfy constraint')



"""Sort a list of numbers using their absolute values; use the abs() function as key"""

l = [1, -4, 9, 2, 2.8]

for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if abs(l[i]) > abs(l[j]):
            temp = l[j]
            l[j] = l[i]
            l[i] = temp
print(l)


"""Count how often each letter occurs in a string (caseinsensitively). You can ignore every
 character that is not a letter. Store the counts in a list of 26 items that all start
at zero. Print the resulting counts. As index you can use ord(letter) - ord("a"), where
letter is a lower case letter"""

lista_alfabeto = [chr(ord('a') + j) for j in range(26)]
lista_nmb = [0]*26
s = 'casa'

for j in range(len(lista_nmb)):
    for lettera in s:
        if chr(ord('a') + j) == lettera:
            lista_nmb[j] += 1

print(lista_nmb)