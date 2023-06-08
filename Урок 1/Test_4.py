# Пишем алгоритм поиска нужного числа последовательности Фибоначчи.
# Считаем, что 1 и 2 значения последовательности равны 1.
# Искать будем по формуле On=On-1+On-2 что предполагает использовать рекурсивного алгоритма.
from datetime import datetime


def next(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return next(n - 1) + next(n - 2)


class Fibo:

    def __init__(self):
        self.number = self.take()
        self.fibo = next(self.number - 1)

    def take(self):
        res = int(input("Какое число фибоначи нужно найти? "))
        return res


begin_time = datetime.now()
N = Fibo()
print('{0:,}'.format(N.fibo).replace(',', ' '))
end_time = datetime.now()
print('Время выполнения кода C РЕКУРСИЕЙ: ', end_time - begin_time)
