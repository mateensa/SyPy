#Author: Mateen SA
#Binary Tree implementation using list data structure

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        # When inserting at level 3 we pass level 2 node as root (not actual root {/})
        # It always adds new branch element to left shifting other nodes to right.
        root.insert(1,[newBranch,t,[]])
    else:
        #If there is only one node (root) in tree then we add branch to root with left and right as empty array elements.
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        #When inserting at level 3 we pass level 2 node as root (not actual root {/})
        #It always adds new branch element to left shifting other nodes to right.
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)  #write first left (new level=2 will be created)
insertLeft(r,5)  #write to level 2 but shift existing nodes to right side
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

# x = BinaryTree('a')
# insertLeft(x,'b')
# insertRight(x,'c')
# insertRight(getRightChild(x),'d')
# insertLeft(getRightChild(getRightChild(x)),'e')

# ['a', ['c', ['b', [], []], [] ] , ['d', [], ['c', [], [] ] ] ]

