# Попытка номер один - не получилось



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

    def __del__(self):

        while self.next != None:
            if self.next.next == None:
                self.next = None
            self = self.next


ll = Node(1)
ll.append(2)
ll.append(3)
ll.__del__()
ll.append(4)
node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)
