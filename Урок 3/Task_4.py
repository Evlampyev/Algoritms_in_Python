# Двухвязный список


class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def appendEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.previous = lastNode
        self.tail = newNode

    def appendFirst(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            self.head = newNode
            self.head.next = n
            n.previous = self.head

    def removeEnd(self):
        if self.tail == None:
            return
        else:
            n = self.tail
            n = n.previous
            n.next = None
            self.tail = n

    def reverseList(self):
        '''
        Развернуть двухсвязный список
        :return:
        '''
        if self.head is None:
            self.printList()
        else:
            n = self.head
            while n is not None:
                temp = n.next
                n.next, n.previous = n.previous, n.next
                n = temp
            self.head, self.tail = self.tail, self.head
            self.printList()

    def printList(self):
        n = self.head
        while n is not None:
            print(n.data, end='-->')
            n = n.next
        print('None')


if __name__ == '__main__':
    dlst = DoubleLinkedList()
    print("Только создали")
    dlst.printList()
    dlst.appendEnd(1)
    print("Добавили 1 конец")
    dlst.printList()

    dlst.appendEnd(2)
    print("Добавили 2 конец")
    dlst.printList()

    print("Добавили 0 в начало")
    dlst.appendFirst(0)
    dlst.printList()
    print("Добавили -1 в начало")
    dlst.appendFirst(-1)
    dlst.printList()

    dlst.appendEnd(3)
    print("Добавили 3 конец")
    dlst.printList()

    print("Удалили 3 в конце")
    dlst.removeEnd()
    dlst.printList()
    print("Развернули")
    dlst.reverseList()

    dlst.appendEnd(-2)
    dlst.appendFirst(3)
    print('Добавили в конец и начало')
    dlst.printList()