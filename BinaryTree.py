#Author: Mateen SA
#Binary Tree implementation using nodes and edges


class BinaryTree:

    def __init__(self, root):
        self.root = root;
        self.leftChild = None;
        self.rightChild = None;

    def setLeftChild(self, root, newNodeValue):

        node = BinaryTree(newNodeValue);

        if self.leftChild == None:
            self.leftChild = node;
        else:
            node.leftChild = self.leftChild;
            self.leftChild = node;

    def setRightChild(self, root, newNodeValue):

        node = BinaryTree(newNodeValue);

        if self.rightChild == None:
            self.rightChild = node;
        else:
            node.rightChild = self.rightChild;
            self.rightChild = node;


    def getLeftChild(self):
        return self.leftChild;

    def getRightChild(self):
        return self.rightChild;

    def getRootValue(self):
        return self.root;

    def setRootValue(self, newRootValue):
        self.root = newRootValue;

    def getNodeValue(self, node):
        return BinaryTree(node).getRootValue();

btree = BinaryTree('a');
btree.setRootValue('A');
print(btree.getRootValue());
btree.setLeftChild('B', btree);
print(btree.getLeftChild().getRootValue());
btree.setRightChild('C', btree);
print(btree.getRightChild().getRootValue())
btree.setLeftChild('D', btree.getLeftChild())
print(btree.getLeftChild().getLeftChild().getRootValue())
btree.setLeftChild('E', btree.getRightChild());
btree.setRightChild('F', btree.getRightChild())
