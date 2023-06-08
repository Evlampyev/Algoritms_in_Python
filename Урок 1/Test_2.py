# Написать алгоритм поиска простых чисел (делятся только на себя и на 1) в диапазоне от 1 до N.
# В алгоритме будет использоваться вложенный for, что явно говорит о квадратичной сложности


from math import sqrt


def check_simplcity(num):
    res = True
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            res = False
            break
    return res


class Number:

    def __init__(self):
        self.number = self.enter()
        self.list_prime_number = []
        if self.number > 1:
            self.list_prime_number.append(1)
        if self.number > 2:
            self.list_prime_number.append(2)
        for i in range(3, self.number + 1):
            if check_simplcity(i):
                self.list_prime_number.append(i)

    def enter(self):
        res = int(input('Введите значение N '))
        return res


N = Number()
print(f"Все простые числа от 1 до {N.number}: ", N.list_prime_number)
