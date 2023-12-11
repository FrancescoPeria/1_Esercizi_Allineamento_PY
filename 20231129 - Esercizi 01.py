7/4 # Non succede niente

print('Hello, World!')

# Esercizi

# 1) Write and run the program which write your 1st and last name
print('Francesco', 'Peria')

# 2) Scrivi un programma che usa tutti gli operatori
a = 5
b = 7
risu = a + b
print(risu)
risu = a * b
print(risu)
risu = a / b
print(risu)

# 1) Scrivere un programma che mostra i secondi in una settiana
seconds = 7*24*60*60
print(seconds)

""" 2) The cover price of a book is €24.95, but bookstores get a 40 percent discount. Shipping costs €3 for the first
copy and 75 cents for each additional copy. Calculate the total wholesale costs for 60 copies"""
price = 24.95
discount = 0.4
shipping_cost_first = 3
shipping_cost_others = 0.75
copie = 100

total_ship = shipping_cost_first + shipping_cost_others*(copie-1) + copie*(1-discount)*price
print(total_ship)

# 3) Write a program that generates the ZeroDivisionError
#print(3/0)

""" 4) You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time
will the alarm go off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator """
start = 14
duration = 1000
end = (start + (duration%24))%24
print(end)

""" 5) Solve previous exercise 1 by assign the calculation to a variable. 
Then add a statement to print the contents of the variable """
name = 'Francesco Peria'
print(name)

