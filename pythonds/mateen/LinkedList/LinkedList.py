from pythonds.mateen.LinkedList import Node;

class LinkedList:

    def __init__(self):
        self.head = None;

    def isEmpty(self):
        return self.head == None;

    def add(self, item):
        temp = Node.Node(item);
        temp.setNext(self.head);
        self.head = temp;

    def size(self):
        currentNode = self.head;
        count = 0;
        while currentNode != Node:
            currentNode = currentNode.getNext();
            count +=1;
        return count;

    def search(self, item):

        found = False;
        currentNode = self.head;
        while currentNode != None and not found:
            if currentNode.getData() == item:
                found = True;
            else :
                currentNode = currentNode.getNext();
                found = False;
        return found;


    def remove(self, item):

        found = False;
        currentNode = self.head;
        previousNode = None;

        while not found and currentNode != None:
            if currentNode.getData() == item :
                found = True;
            else :
                previousNode = currentNode;
                currentNode = currentNode.getNext();

        if previousNode == None:
            self.head = currentNode.getNext();
        else:
            previousNode.setNext(currentNode.getNext());

        return currentNode.getData();

    def getAllElements(self):

        l = [];
        found = False;
        currentNode = self.head;

        while not found and currentNode != None:

            if currentNode.getNext() != None:
                l.append(currentNode.getData());
                currentNode = currentNode.getNext();
            else:
                found = True;
        l.append(currentNode.getData());
        return l;

    def append(self, item):
        temp = Node.Node(item);
        temp.setNext(self.head);
        self.head = temp;
        return temp.getData();



li = LinkedList();
li.add(10);
li.add("Apple");
li.add(20);
li.add(True);
li.add("Apple");
li.add(200.9);
print(li.getAllElements())

print(li.remove(10))
print(li.getAllElements())
print(li.append(2222))
print(li.append(2222))
print(li.getAllElements())