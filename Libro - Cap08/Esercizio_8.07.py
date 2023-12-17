"""What is wrong with the following code? Fix it!"""


# What is wrong?
def area_of_triangle(bottom, height):
    area = 0.5 * bottom * height
    print("The area of a triangle with a bottom of", bottom, "and a height of", height, "is", area)


print(area_of_triangle(4.5, 1))

"""Non c'è un valore di return nella funzione, ma al contrario c'è una print.
Quindi quando viene fatto print(area_of_triangle(a, b)), non essendoci un return, ottengo un null"""


def area_of_triangle(bottom, height):
    area = 0.5 * bottom * height
    return area


a = 4.5
b = 1
print("The area of a triangle with a bottom of", a, "and a height of", b, "is", area_of_triangle(a, b))
