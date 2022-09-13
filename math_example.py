import math


# a = 14578
# count_of_nums = 1000

# print ('Число', a, ' - это ')
# print (a // count_of_nums)
# print ('и')
# print (a % count_of_nums)



n = 32.95467
drob = 0.95467

num = math.trunc(n)
print(num)

num = math.floor(n)
print(num)

num = math.ceil(n - drob + 0.00001)
print(num)