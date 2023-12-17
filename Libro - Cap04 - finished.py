"""4.1) Define three variables v1, v2 and v3. Calculate the average of these
variables and assign it to avg. Print the average. Add three comments."""

v1 = 1
v2 = 2
v3 = 3
avg = (v1 + v2 + v3) / 3
print('Media variabili v1, v2, v3: ', avg)


"""4.2) Write code that can compute the surface of circle, using the variables radius
and pi = 3.14159. The formula, in case you do not know, is radius times radius times pi.
Print the outcome of your program as follows: “The surface area of a circle with radius ... is ..."""
import math
r = 3
area = math.pi * r**2
print("The surface area of a circle with radius {} is {}".format(r, round(area, 2)))

"""4.3) Write code that classifies a given amount of money (which you store in a
variable named amount), specified in cents, as greater monetary units. Your code lists the
monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and
pennies (1 ct). Your program should report the maximum number of dollars that fit in the
amount, then the maximum number of quarters that fit in the remainder after you subtract
the dollars, then the maximum number of dimes that fit in the remainder after you subtract
the dollars and quarters, and so on for nickels and pennies. The result is that you express
the amount as the minimum number of coins needed"""

amount = 4312
dollars = int(amount/100)
remainder = amount % 100
quarters = int(remainder/25)
remainder = remainder % 25
dimes = int(remainder / 10)
remainder = remainder % 10
nickels = int(remainder / 5)
penny = remainder

print(f'The amount {amount} consists of:\ndollars: {dollars}\nquarters: {quarters}\ndimes: {dimes}\nnickels: {nickels}\npenny: {penny}')


"""4.4) Can you think of a way to swap the values of two variables that does not
need a third variable as a temporary storage? In the code block below, try to implement
the swapping the values of A and B without using a third variable. To help you out, the
first step to do this is already given. You just need to add two more lines of code."""
a = 17
b = 23
print('a = ', a, 'and b = ', b)
a += b
b = a - b
a = a - b
print('a = ', a, 'and b = ', b)
