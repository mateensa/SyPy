class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        return self.performGateLogic()


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n);

        self.pinA = None;
        self.pinB = None;

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter value of Pin A "+self.getLabel()));
        else:
            return self.pinA.getFrom().getOutput()


    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter value of Pin B "+self.getLabel()));
        else:
            return self.pinB.getFrom().getOutput();

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n);
        self.pin = None;

    # Another way of calling parent class constructors but specially used if there are multiple parent classes
    # def __init__(self, n):
    #     super(UnaryGate, self).__init__(n);

    def getPin(self):
        if self.pin == None:
            return int(input("Enter value of Pin "+self.getLabel()))
        else:
            return self.pin.getFrom().getOutput();

    def performGateLogic(self):
        pinValue = self.getPin();
        return 1 if pinValue == 0 else 0;

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source;
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n);

    def performGateLogic(self):
        pinA = self.getPinA();
        pinB = self.getPinB();

        if pinA == 1 and pinB == 1 :
            return 1
        else:
            return 0;

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source;
        else:
            if self.pinB == None:
                self.pinB = source;
            else:
                raise RuntimeError("Cannot connect to Pin A and Pin B, Both pins are already connected")



class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n);

    def performGateLogic(self):
        pinA = self.getPinA();
        pinB = self.getPinB();

        if pinA == 1 or pinB == 1 :
            return 1
        else:
            return 0;

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source;
        else:
            if self.pinB == None:
                self.pinB = source;
            else:
                raise RuntimeError("Cannot connect to Pin A and Pin B, Both pins are already connected")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n);

    def performGateLogic(self):
        if self.getPin():
            return 0;
        else:
            return 1;

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate;
        self.togate = tgate;

        tgate.setNextPin(self);

    def getFrom(self):
        return self.fromgate;

    def getTo(self):
        return  self.togate;


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()