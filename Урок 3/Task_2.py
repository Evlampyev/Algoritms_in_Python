# Попытка номер 2 реализация не верная, без класса LinkedList



# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def appendEnd(self, val):
        end = Node(val)
        n = self
        while n.next:
            n = n.next
        n.next = end

    def appendFirst(self, val):
        first = Node(val)
        if head.next == None:
            self = first
        else:
            first.next = head

    def removeLast(self):
        n = self
        if n.next is None:
            self.data = None
        else:
            while n.next:
                if n.next.next is None:
                    n.next = None
                else:
                    n = n.next


# Функция для печати заданного связанного списка
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=' —> ')
        ptr = ptr.next

    print('None')


# Функция построения связанного списка из заданного набора ключей
def construct(keys):
    head = None

    # начать с конца списка
    for i in reversed(range(len(keys))):
        # выделяет новый узел в куче и устанавливает его данные
        head = Node(keys[i], head)

    return head


if __name__ == '__main__':
    # Клавиши ввода
    keys = [1, 2, 3, 4]

    # указывает на головной узел связанного списка
    head = construct(keys)

    # распечатать связанный список
    printList(head)

    head.appendEnd(5)
    printList(head)

    head.removeLast()
    printList(head)
    head.appendEnd(6)
    printList(head)

    head.appendFirst(10)
    printList(head)
