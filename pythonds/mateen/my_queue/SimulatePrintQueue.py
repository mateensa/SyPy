from pythonds.mateen.my_queue import Printer, Task, My_Queue;
from random import randrange;

def simulate(noOfSeconds, ppm):

    labPrinter = Printer.Printer(ppm);
    printQueue = My_Queue.Queue();
    waitingTimes = [];

    for eachSecond in range(noOfSeconds):
        if newPrintTask():
            task = Task.Task(noOfSeconds);
            printQueue.enqueue(task);

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue();
            waitingTimes.append(nextTask.waitTime(eachSecond));
            labPrinter.startNext(nextTask);

        labPrinter.tick();
        averageWait = 0 if len(waitingTimes) == 0 else sum(waitingTimes) / len(waitingTimes);
        print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    num = randrange(1, 181);
    return num == 180;

for i in range(10):
    simulate(3600, 5);
