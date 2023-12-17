for j in range(1, 100):
    for k in range(1, 100):
        nmb = j**2 + k**2
        if nmb < 100:
            print(f'{j}**2 + {k}**2 = {nmb}')
