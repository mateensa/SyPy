from time import time;
from random import randrange;

class Task:

    def __init__(self, time):
        self.timestamp = time;
        self.pages = randrange(1, 21);

    def getTimestamp(self):
        return self.timestamp;

    def getPages(self):
        return self.pages;

    def waitTime(self, currenttime):
        return currenttime - self.timestamp;

