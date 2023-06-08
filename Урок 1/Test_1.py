class Number:

    def __init__(self):
        self.number = self.take()
        self.sum_numbers = self.calculate_sum()

    def take(self):
        '''
        Ввод с клавиатуры аттрибута number
        :return:
        '''
        res = int(input('Введите число N: '))
        return res

    def calculate_sum(self):
        '''
        Метод считает сумму чисел от 0 до N
        :return:
        '''
        result = 0
        n = self.number
        for i in range(1, n + 1):
            result += i
        return result

    def print_num(self):
        '''
        Метод выводит на экран сумму чисел
        :return:
        '''
        print(f'Сумма от 1 до {self.number} = ', self.sum_numbers)


print("Начало программы")
N = Number()
N.print_num()
S = Number()
S.print_num()
