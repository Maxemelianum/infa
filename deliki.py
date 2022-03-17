delitil = []

for numbers in range(174457, 174505):
    for d in range(2, int(numbers**0.5)+1):
        if numbers % d == 0:
            delitil.append(d)
            delitil.append(numbers // d)
        if len(delitil) > 2:
            break
    if len(delitil) == 2:
        print(numbers, delitil)

    delitil = []