from pythonds.mateen.LinkedList import Node;

class OrderedList:

    def __init__(self):
        self.head = None;

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node.Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        currentNode = self.head;
        found = False;
        while currentNode != None and not found:
            if currentNode.getData() != item:
                currentNode = currentNode.getNext();
            else :
                found = True;

        return found;

    def isEmpty(self):
        return self.head == None;

    def size(self):
        counter = 0 ;
        currentNode = self.head;
        while currentNode != None:
            currentNode =  currentNode.getNext();
            counter +=1;
        return counter;

    def index(self, item):
        counter = 0;
        currentNode = self.head;
        while currentNode != None :
            if currentNode.getData() != item:
                counter +=1;
                currentNode = currentNode.getNext();
            else:
                break;
        return 0 if currentNode == None else counter;

    def remove(self, item):
        currentNode = self.head;
        if self.size() == 1 and currentNode.getData() == item:
            self.head = None;
            return currentNode.getData();

        previousNode = None;
        found = False;

        while currentNode != None and not found:
            if currentNode.getData() == item:
                found = True;
            else:
                previousNode = currentNode;
                currentNode = currentNode.getNext();

        if previousNode == None:
            previousNode = self.head;
            currentNode = currentNode.getNext();
            self.head = currentNode;
            return previousNode.getData();
        else:
            previousNode.setNext(currentNode.getNext())
            self.head = previousNode;
            return currentNode.getData();

    def pop(self, item):
        self.remove(item);

    def pop(self, index):

        if index == 0 or self.size() == 0 :
            return "Opration not allowed size is zero"

        counter = 0;
        currentNode = self.head;
        previousNode = None;

        while counter <= index and currentNode != None:
            previousNode = currentNode;
            currentNode = currentNode.getNext();
        previousNode.setNext(currentNode.getNext());
        return currentNode.getData();

    def getElements(self):

        li = [];
        currentNode = self.head;

        while currentNode != None:
            li.append(currentNode.getData());
            currentNode = currentNode.getNext();

        return li;


olist = OrderedList();
# print(olist.isEmpty())
olist.add(17);
olist.add(26);
olist.add(1000);
olist.add(9.9999);
olist.add(200);
olist.add(300);
olist.add(800);
print(olist.getElements());
print(len(olist.getElements()))
print(olist.size())
print(olist.search(100))
print(olist.search(500))
print(olist.isEmpty())
print(olist.index(0))
print(olist.index(10))
print(olist.index(9.9999))
print(olist.remove(800))
print(olist.getElements())