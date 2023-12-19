"""Create a function that gets a number as parameter, and then prints the
multiplication table for that number from 1 to 10. E.g., when the parameter is 12, the first
line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120"""

def my_func(N):
    j = 1
    while(j <= 10):
        print(f'{j} * {N} = ', j * N)
        j += 1

if __name__ == '__main__':
    my_func(12)