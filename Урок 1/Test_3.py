# Необходимо написать алгоритм поиска всех доступных комбинаций (посчитать количество) для 4 кубиков с количеством граней N.
# Данное решение имеет сложность O(n4), но если количество кубиков сделать переменной, то она трансформируется в O(nk),
# что будет представлять собой экспоненциальную сложность.

class Kub:

    def __init__(self):
        self.edge = self.print_edge()
        ed = self.edge
        self.count = 0
        for i in range(1, ed + 1):
            for j in range(1, ed + 1):
                for k in range(1, ed + 1):
                    for l in range(1, ed + 1):
                        print(i, j, k, l)
                        self.count += 1

    def print_edge(self):
        res = int(input("Укажите количество граней на кубике - "))
        return res


kub = Kub()
print(kub.count)
