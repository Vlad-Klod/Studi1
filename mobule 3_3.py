print(f'Задача - "Распаковка"')
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(c=[23,22,54])
values_list = ["Добрый день!", 55, [77,19,False]]
values_dict = {'a':74, 'b':True, 'c':"Спокойной ночи!"}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [34.76, 'Успешного дня!']
print_params(*values_list2, 42)