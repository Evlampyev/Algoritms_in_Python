# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Связный список
class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def appendEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode

    def appendFirst(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def printList(self):
        n = self.head
        while n:
            print(n.data, end='-->')
            n = n.next
        print('None')

    def removeEnd(self):
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
        n = self.head
        if n is None:
            return
        else:
            self.head = n.next

    def contain(self, val):
        n = self.head
        while n is not None:
            if n.data == val:
                return True
            else:
                n = n.next

        return False


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
    if lst.contain(3):
        print('In')
    else:
        print('No in')
