"""A complex number is a number of the form i, whereby and are
constants, and i is a special value that is defined as the square root of -1. Of course, you
never try to actually calculate what the square root of -1 is, as that gives a runtime error; in
complex numbers, you always let the i remain. For instance, the complex number 3 + 2i
cannot be simplified any further.
Addition of two complex numbers a + bi and c + di is defined as (a+c) + (b+d)i. Represent a complex number as a tuple of two numeric
values, and create a function that calculates the addition of two complex numbers"""

def complex_sum(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def print_complex(t):
    print(str(t[0]) + ' + ' + str(t[1])+' i')

complex1 = (1, 6)
complex2 = (2, 8)
print_complex(complex_sum(complex1, complex2))