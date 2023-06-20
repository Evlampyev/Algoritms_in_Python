# Односвязный список


# Узел односвязанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Связный список
class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def appendEnd(self, val):
        '''
        Добавление в конец списка
        :param val: значение
        :return:
        '''
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode

    def appendFirst(self, val):
        '''
        Добавление в начало списка
        :param val: значение
        :return:
        '''
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def printList(self):
        '''
        печать листа
        :return:
        '''
        n = self.head
        while n:
            print(n.data, end='-->')
            n = n.next
        print('None')

    def removeEnd(self):
        '''
        уделение последнего элемента
        :return:
        '''
        n = self.head
        if n.next == None:
            self.data = None
        else:
            while n.next:
                if n.next.next == None:
                    n.next = None
                else:
                    n = n.next

    def removeFirst(self):
        '''
        удаление первого элемента
        :return:
        '''
        n = self.head
        if n is None:
            return
        else:
            self.head = n.next

    def contain(self, val):
        '''
        Проверка наличия элемента
        :param val: какой элемент ищем
        :return:
        '''
        n = self.head
        while n is not None:
            if n.data == val:
                return True
            else:
                n = n.next

        return False

    def searchN(self, N):
        s = self.head
        templist = LinkedList()
        count = 0
        while s is not None:
            if count < N:
                templist.appendEnd(s.data)
                count += 1
            else:
                templist.removeFirst()
                templist.appendEnd(s.data)
            s = s.next
        answer = templist.head.data
        return answer


if __name__ == '__main__':
    lst = LinkedList()
    lst.printList()
    lst.appendEnd(1)
    lst.appendEnd(2)
    lst.printList()
    lst.appendFirst(0)
    lst.printList()
    # lst.removeEnd()
    # lst.removeFirst()
    # lst.removeFirst()

    lst.printList()
    s = 3
    if lst.contain(s):
        print(f'{s} In List')
    else:
        print(f'{s} No in List')

    lst.appendEnd(3)
    lst.appendFirst(-1)
    print('Итогвый лист для поиска')
    lst.printList()

    serch = 2
    print(f"Ищем {serch} элемент с конца")
    print(lst.searchN(serch))
