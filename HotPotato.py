import My_First_Queue;

def simulateHotPotato(nameList, noOfPasses):

    q = My_First_Queue.Queue();
    for name in nameList:
        q.enqueue(name);

    while q.size() > 1:
        for i in range(noOfPasses):
            q.enqueue(q.dequeue());
        q.dequeue();
    return q.dequeue();



print(simulateHotPotato(["Bill", "Brad", "Kent", "Jane", "Susan", "David"], 15));
