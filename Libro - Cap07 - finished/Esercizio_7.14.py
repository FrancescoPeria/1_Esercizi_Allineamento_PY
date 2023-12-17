"""A, B, C, and D are all different digits. The number DCBA is equal to 4 times
the number ABCD. What are the digits? Note: to make ABCD and DCBA conventional
numbers, neither A nor D can be zero. Use a quadruple-nested loop"""

for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(1, 10):
                nmb_1 = i*1000 + j*100 + k*10 + l
                nmb_2 = l*1000 + k*100 + j*10 + i
                if nmb_2 == 4*nmb_1:
                    print('The digits are: ', i, j, k, l)