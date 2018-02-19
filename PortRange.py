class PortRange:
    lower = None
    upper = None
    ports = None

    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper
        self.ports = int(upper) - int(lower)

    def printRange(self):
        print("%s - %s (%s ports)" % (self.lower.decode("utf-8"),self.upper.decode("utf-8"), self.ports))