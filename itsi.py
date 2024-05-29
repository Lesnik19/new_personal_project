# n = set()  # Подходящие числа
# for x in range(22333, 89000):
#     ds = set()  # Делители числа
#     for d in range(1, round(x**0.5)+1):
#      # Рассматриваем парные множители
#         if x % d == 0:
#             if d % 2 != 0:
#                 ds.add(d)
#             if (x//d) % 2 != 0:
#                 ds.add(x//d)
#         # Если делителей уже больше 3, то прекращаем работу цикла
#         if len(ds) > 3:
#             break
#     if len(ds) == 3:
#         n.add(x)
# print(len(n))

# Вариант 3
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [775240; 778900], числа,
# кратные сумме цифр самого числа. В качестве ответа запишите количество таких чисел.

# n = []
#
# for x in range(775240, 778901):
#     number = x
#     sum_n = 0
#     while number > 0:
#         sum_n += number % 10
#         number = number // 10
#     if x % sum_n == 0:
#         n.append(x)
# print(len(n))


num = int(input('Введите число от 1 до 10000: '))
answer = 0
for i in range(1, num + 1):
    if i % 10 == 7:
        long = 0
        for a in str(num):
            long += 1
        if long == 1:
            if i == 7:
                answer += 1
        elif long == 2:
            num1 = i % 10
            num2 = i // 10
            if (num1 != num2 and num1 * num2 < 9) or (num1 == num2 and i < 9):
                answer += 1
        elif long == 3:
            num1 = i % 10
            num2 = i // 10 % 10
            num3 = i // 100
            if ((num1 != num2 and num2 != num3 and num3 != num1 and num1 * num2 * num3 < 9) or
                    (num1 == num2 and num3 * num2 < 9) or (num2 == num3 and num3 * num1 < 9) or
                    (num1 == num3 and num3 * num2 < 9)):
                answer += 1
        elif long == 4:
            num1 = i % 10
            num2 = i // 10 % 10
            num3 = i // 100 % 10
            num4 = i // 1000
            if ((num1 != num2 and num2 != num3 and num3 != num1 and num1 != num4 and num2 != num4 and num3 != num4 and
                 num1 * num2 * num3 * num4 < 9) or (num1 == num2 and num3 * num2 * num4 < 9) or
                    (num2 == num3 and num3 * num1 * num4 < 9) or (num1 == num3 and num3 * num2 * num4 < 9) or (num1 == num4 and num3 * num2 * num4 < 9) or
                    (num2 == num4 and num3 * num1 * num4 < 9) or (num4 == num3 and num3 * num2 * num1 < 9)):
                answer += 1
print(answer)

ni = 1000
print(ni % 10)
print(ni // 10 % 10)
print(ni // 100 % 10)
print(ni // 1000)
print((ni % 10) * (ni // 10 % 10) * (ni // 100 % 10) * (ni // 1000))
