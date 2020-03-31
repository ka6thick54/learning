class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addChild(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode

    def printAsArray(self):
        arrayRep = []
        print(self.printNode(self, arrayRep))

    def printNode(self, node, arrayRep):
        if node.value in arrayRep:
            index = arrayRep.index(node.value)+1
        else:
            index = 1
            arrayRep.insert(index - 1, node.value)
        leftIndexToInsert = (2*(index)) - 1
        rightIndexToInsert = leftIndexToInsert + 1
        if(node.left is not None):  
            arrayRep.insert(leftIndexToInsert, node.left.value)
            self.printNode(node.left, arrayRep)
        else:
            arrayRep.insert(leftIndexToInsert, None)
        if(node.right is not None):
            arrayRep.insert(rightIndexToInsert,node.right.value)
            self.printNode(node.right, arrayRep)
        else:
            arrayRep.insert(rightIndexToInsert, None)
        return arrayRep


root = Node(10)
leftChild = Node(8)
rightChild = Node(9)
rightChild.addChild(Node(7),Node(6))
root.addChild(leftChild,rightChild)

root.printAsArray()
