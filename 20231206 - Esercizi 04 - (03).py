"""1) Write a program that reads an integer number n, creates
a list that contains the first n positive integers, and prints it"""

N = int(input('Inserisci un numero: '))
lista = []
j = 1
while j <= N:
    lista.append(j)
    j += 1
print(lista)


""" 2) Write a program that reads from input a list of n integers and displays the sum, 
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

