"""1) Write and test a function is_even()"""
def is_even(n):
    return n % 2 == 0


"""2) Write and test a function isOdd(), which determines whether a number is odd,
 by calling the function isEven() and inverting its result"""
def is_odd(n):
    return not is_even(n)


"""3) Write and test a function getFraction() that gets the fractional part of a float (i.e., the decimals)"""
def get_fraction(n):
    return n - int(n)


"""4) Write and test a function that returns the number of days in A years, B months and C weeks?"""
def get_days(Years, Months, Weeks):
    return Years*365 + Months*30 + Weeks*7


"""5) Define a function called distance_from_zero, with one argument. If the type of the argument is either
int or float, the function returns the absolute value of the input. Otherwise, the function returns \"Nope\""""

def distance_from_zero(x):
    if isinstance(x, int) or isinstance(x, float):
        return abs(x)
    else:
        return "Nope"



def main():

    """Test funzione 1)"""
    print('Test funzione 1)')
    N = int(input('Inserisci un intero: '))
    if is_even(N):
        print(f'Il numero {N} è pari')
    else:
        print(f'Il numero {N} è dispari')


    """Test funzione 2)"""
    print('Test funzione 2)')
    N = int(input('Inserisci un intero: '))
    if is_odd(N):
        print(f'Il numero {N} è dispari')
    else:
        print(f'Il numero {N} è pari')


    """Test funzione 3)"""
    print('Test funzione 3)')
    N = float(input('Inserisci un numero: '))
    print(f'Parte frazionaria di {N}: ', get_fraction(N))


    """Test funzione 4)"""
    print('Test funzione 4)')
    anni = float(input('Inserisci un numero di anni: '))
    mesi = float(input('Inserisci un numero di mesi: '))
    sett = float(input('Inserisci un numero di settimane: '))
    print('In totale abbiamo: ', get_days(anni, mesi, sett), ' giorni')


    """Test funzione 5)"""
    print('Test funzione 5)')
    x = float(input('Inserisci un numero: '))
    print(f'Distanza da 0 per il numero {x} --> ', distance_from_zero(x))



if __name__ == '__main__':
    main()
