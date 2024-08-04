print(f'Задача - "Все не так уж и просто!"')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
non_prime = []
prime = []
is_prime = False
for i in range(2, 16):
    k = 2
    while k * k <= i:
        if i % k == 0:
            is_prime = True
            if is_prime:
                non_prime.append(i)
            break
        k += 1
    else:
        prime.append(i)
print((prime), '- простые')
print((non_prime), '- составные')
