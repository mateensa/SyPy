from math import pi;

class MyCircle:

    def __init__(self):
        self.__radius__ = None;

    def setRadius(self, radius):
        self.__radius__ = radius;

    def getRadius(self):
        return self.__radius__;

    def getArea(self):
        """
        This is a reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """
        return pi * self.__radius__ ** 2;

    def __add__(self, anotherCircle):
        crcle = MyCircle();
        crcle.setRadius(self.__radius__ + anotherCircle.__radius__);
        return crcle;

c = MyCircle();
c.setRadius(1);
print(c.getArea())

c2 = MyCircle();
c2.setRadius(1);
print((c+c2).getArea());