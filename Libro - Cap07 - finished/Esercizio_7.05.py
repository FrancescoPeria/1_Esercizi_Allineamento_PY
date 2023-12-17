"""The Fibonacci sequence is a sequence of numbers that starts with 1, followed
by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence
starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a program that calculates and prints the Fibonacci
sequence until the numbers get higher than 1000"""

prec2 = 1
prec1 = 1
print(f'Serie Fibonacci: {prec1}')
print(f'Serie Fibonacci: {prec2}')
while True:
    if prec1 + prec2 >= 1000:
        break
    sum = prec1 + prec2
    print(f'Serie Fibonacci: {sum}')
    prec2 = prec1
    prec1 = sum

