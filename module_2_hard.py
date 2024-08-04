print(f'Задача - "Cлишком древний шифр!"')
def password_selection (n):
    password = ''
    for i in range (1,n):
        for j in range (i + 1, n):
            if n % (i+j) == 0:
                password += str (i) + str (j)
    return password
for n in range (3, 21):
    password = password_selection(n)
    print(f'Если Вам выпало число {n} - то для спасения введите число - {password} ')



