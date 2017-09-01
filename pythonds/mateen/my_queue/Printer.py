class Printer:

    def __init__(self, ppm):
        self.pagerate = ppm;
        self.currentTask = None;
        self.timeRemaning = 0;

    def tick(self):
        if self.currentTask != None:
            self.timeRemaning = self.timeRemaning - 1;
            if self.timeRemaning <= 0:
                self.currentTask = None;


    def busy(self):
        return True if not self.currentTask == None else False;

    def startNext(self, task):
        self.currentTask = task;
        self.timeRemaning = task.getPages() * 60 / self.pagerate;

