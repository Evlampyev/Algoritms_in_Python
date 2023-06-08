# Пишем алгоритм поиска нужного числа последовательности Фибоначчи, но в этот раз откажемся от рекурсии и
# воспользуемся обычным алгоритмом, что даст нам линейную сложность, т.к. вычисление каждого из чисел
# последовательности будет происходить ровно 1 раз.

from datetime import datetime


class Fibo:

    def __init__(self):
        self.number = self.take()
        self.fibo = self.fibon()

    def take(self):
        res = int(input("Какое число Фибоначчи нужно найти? "))
        return res

    def fibon(self):
        n = self.number
        res = -1
        if n == 1:
            res = 0
        elif n == 2:
            res = 1
        else:
            step = 3
            first = 0
            second = 1
            while step <= n:
                res = first + second
                first = second
                second = res
                step += 1
            return res


begin_time = datetime.now()
N = Fibo()
print('{0:,}'.format(N.fibo).replace(',', ' '))
end_time = datetime.now()
print('Время выполнения кода без рекурсии: ', end_time - begin_time)
