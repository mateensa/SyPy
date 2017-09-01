class Queue:

    def __init__(self):
        self.items = [];

    def isEmpty(self):
        return self.items == [];

    def size(self):
        return len(self.items);

    def enqueue(self, item):
        self.items.insert(0, item);

    def dequeue(self):
        return self.items.pop();

    def getElements(self):
        return self.items;

# q = Queue();
# q.enqueue('hello');
# q.enqueue('dog');
# q.enqueue(3);
# q.dequeue();
# print(q.getElements())





# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def enqueue(self, item):
#         self.items.insert(0,item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
