string_example = '''

!!!
HELLO WORLD
!!!

'''

# print(string_example)

h = 'Hello'
w = 'world'
space = ' '
multiple = 1

grus = (h + space + w + '!\n\n') * multiple
print(grus)

print(len(grus))

print(ord('A'))

print(ord(grus[-1]))
print(grus[::2])

# ------------------------

upper_grus = grus.upper()
print(upper_grus)

lower_grus = upper_grus.lower()
print(lower_grus)

count_grus = grus.count('\n')
print(count_grus)

find_grus = grus.find('wor')
print(find_grus)

index_grus = grus.index('wor')
print(index_grus)

replace_grus = grus.replace('\n', '')
print(replace_grus)

strip_grus = grus.strip()
print(strip_grus)

lstrip_grus = grus.lstrip()
print(lstrip_grus)

alfab_grus = not(grus.isalpha())
print(alfab_grus)

# string.isdigit()

list_grus = grus.split()
print(list_grus)

join_grus = '+'.join(list_grus)
print(join_grus)

# new_grus = input().upper()
# print(new_grus)

# --------------------------------------------

name = 'Иван'
mid_name = 'Иваныч'

balance = 234.11

divide = '=================================='

text = '''
{d}

Уважаемый, {n} {m}, ваш баланс\n равен {b} рублей

{d}
'''.format(n=name,m=mid_name,b=balance,d=divide)

print(text)


# F-строки

text = f'''
{divide}

Уважаемый, {name} {mid_name.upper()}, ваш баланс\n равен {balance} рублей

{divide}
'''

# print(text,'\n\n\')

gender = {
  'm':'Уважаемый',
  'f':'Уважаемая'
  }

abonents = [
  ['Иван', 'Иваныч', 0,'m'],
  ['Пенелопа', 'Сегизмундовна', 5473.12,'f'],
  ['Никанор', 'Петрович', 124.63,'m']
]

for name,mid_name,balance,g in abonents:
  text = f'''{divide}\n{gender[g]} {name} {mid_name.upper()},\n ваш баланс {balance} рублей\n{divide.replace('=','-')}'''
  print(text)