# # Задиние № 1

from sys import argv
name, hours, rate_per_hour, reward = argv

def salary(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    total_salary = a * b + c
    print(total_salary)

salary(hours, rate_per_hour, reward)

# Задание № 2 - не знаю как сделать

orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in orig_list if el > orig_list[orig_list.index(el) - 1]]

print(new_list)

# Задание № 3

count_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(count_list)

# Задание № 4

original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in original_list if (original_list.count(el) == 1)]
print(new_list)

# Задание № 5

from functools import reduce

def calc(a, b):
    return a * b

count_list = [el for el in range(100, 1001) if el % 2 == 0 ]

print(reduce(calc, count_list))

# Задание № 6

from itertools import count, cycle

i = int(input('Введите число: '))
end_point = 0
for el in count(i):
    if end_point == 15:
        break
    else:
        print(el)
        end_point +=1

break_point = 0
for el in cycle([1, 34.5, 'Tom', False]):
    if break_point == 10:
        break
    else:
        print(el)
        break_point +=1

# Задание № 7

# Я не могу решить зание, т.к. не понимаю что от меня требуется.
# Поясните, пожалуйста, подробнее что требуется в задании