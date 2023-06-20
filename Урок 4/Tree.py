import random


class RBNode:
    def __init__(self, value=None, red=False, parent=None, left=None, right=None):
        self.value = value
        self.red = red
        self.parent = parent
        self.left = left
        self.right = right


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def __repr__(self):
        lines = []
        printTree(self.root, lines)
        return '\n'.join(lines)

    def add(self, val):
        newNode = RBNode(val, True, None, self.nil, self.nil)
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.value < current.value:
                current = current.left
            elif newNode.value > current.value:
                current = current.right
            else:
                return
        newNode.parent = parent
        if parent is None:
            self.root = newNode
        elif newNode.value < parent.value:
            parent.left = newNode
        else:
            parent.right = newNode

        self.fixInsert(newNode)

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, newNode):
        while newNode != self.root and newNode.parent.red:
            if newNode.parent == newNode.parent.parent.right:
                u = newNode.parent.parent.left
                if u.red:
                    u.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rotateLeft(newNode.parent.parent)
            else:
                u = newNode.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.rotate_left(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rotate_right(newNode.parent.parent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr


def printTree(node, lines, level=0):
    if node.value != 0:
        printTree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.value) + ' ' + ('r' if node.red else 'b'))
        printTree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num - 1))
    return nums


if __name__ == "__main__":
    tree = RBTree()
    for x in range(1, 9):
        tree.add(x)
    print(tree)
