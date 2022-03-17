def is_simple(n):
    for d in range(2, int(n ** 0.5)+1):
        if n % d == 0:
            return False
        return True
n = 0
for number in range(245690, 245756):
    n += 1
    if is_simple(number):
        print(n, number)





