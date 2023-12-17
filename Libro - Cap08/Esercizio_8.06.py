"""In statistics, the binomial coefficient indexed by and (often expressed as
“n over k,” whereby must be bigger than or equal to ) is calculated as n!/(k!*(n-k)!
whereby n! indicates the factorial of . As I explained in Chapter 7: the factorial of a
positive integer is that integer, multiplied by all positive integers that are lower (excluding
zero). You write the factorial as the number with an exclamation mark after it. E.g., the
factorial of 5 is 5! = 5 * 4 * 3 * 2 * 1 = 120. If you did all the exercises until now, you
wrote some code for this. Write a function that calculates the binomial coefficient for its
two parameters, and returns the value. Write the code in such a way that it can be used as
a module by another program (i.e., put the tests of your program in a main() function that
is called as explained above"""

def factorial(N):
    fact = N
    j = N-1
    while j > 0:
        fact *= j
        j -= 1
    return(fact)

def binomial_coef(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))


def main():
    n = int(input('Inserisci n: '))
    k = int(input('Inserisci k: '))
    print(f'Coefficiente binomiale di parametri n: {n} e k: {k} --> ', binomial_coef(n, k) )

if __name__ == '__main__':
    main()
