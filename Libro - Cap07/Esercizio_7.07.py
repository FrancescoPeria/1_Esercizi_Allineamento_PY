import random
N = 0
M = 0

while N < 10000000:
    x = random.random()
    y = random.random()
    modulo = (x**2 + y**2) ** (1/2)
    if modulo <= 1:
        M += 1
    N += 1

"""Probabilità che il vettore (x, y) abbia modulo inferiore a 1, che teoricamente vale pi/4"""
probability = M/N
pi_empirico = 4*probability
print(f'La stima empirica di pi è: {pi_empirico}')
