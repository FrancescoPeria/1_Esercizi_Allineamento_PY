"""In Chapter 6 you were asked to implement the quadratic formula to solve
quadratic equations. A quadratic equation is described by three numeric values, usually
called A, B, and C. It has zero, one, or two solutions, depending on the discriminant (the
part under the square root). Write a function that solves a quadratic equation.
As parameters it gets A, B, and C. It returns three values. The first is an integer that indicates the
number of solutions. The second is the first solution. The third is the second solution. Any
of the solutions that do not exist, you can return as zero"""

def solve_equations(A, B, C):

    delta = B ** 2 - 4 * A * C
    N_sol = 0
    if (B == A == 0 and C != 0) or delta < 0:
        N_sol = 0
        sol1, sol2 = 0, 0  # Se l'equazione è impossibile ritorno 0
    elif delta == 0:
        N_sol = 1
        sol1, sol2 = -B / (2 * A), -B / (2 * A)
    else:
        N_sol = 2
        sol1 = (-B + (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
        sol2 = (-B - (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
    return N_sol, sol1, sol2


input_A = int(input('Inserisci A: '))
input_B = int(input('Inserisci B: '))
input_C = int(input('Inserisci C: '))

print('Numero Soluzioni: ', solve_equations(input_A, input_B, input_C)[0])
print('Soluzione 1: ', solve_equations(input_A, input_B, input_C)[1])
print('Soluzione 2: ', solve_equations(input_A, input_B, input_C)[2])
