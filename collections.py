def ler_list():
    print('Тема: списки, кортежи и словари')
    print('\v')
    print('Список или list')
    exmp_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    print(type(exmp_list))
    print(exmp_list)
    print(exmp_list[5])
    print(len(exmp_list))
    exmp_list.insert(7, 'четверг')
    print(exmp_list.count('четверг'))  # сколько раз в списке появляется искомый элемент
    print(exmp_list.index('четверг'))
    print(exmp_list.index('четверг',
                          exmp_list.index('четверг') + 1,
                          len(exmp_list)))

    print(min(exmp_list))
    print(max(exmp_list))


print('\v')
print('Кортеж или tuple')

exmp_tuple = ('Меркурий', 'Венера', 'Земля', 'Марс')
print(type(exmp_tuple))
print(exmp_tuple)
len_exmp_tuple = len(exmp_tuple)
print(len_exmp_tuple)
last_exmp_tuple = exmp_tuple[len_exmp_tuple - 1]
print(last_exmp_tuple)
# exmp_tuple.insert(last_exmp_tuple, 'Юпитер') # AttributeError: 'tuple' object has no attribute 'insert'


print('\v')
print('Словарь или dict')
exmp_dict = {
    'oss': ['Linux', 'Windows', 'BSD'],
    'networks': ('IPv4', 'Mask', 'Gateway')
}
print(type(exmp_dict))
print(list(exmp_dict))
print(exmp_dict['oss'])
oss = exmp_dict['oss']

print(type(oss))
print(oss[0])
# print(exmp_dict.get(oss[1]))