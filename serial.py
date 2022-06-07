"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        "Create serial number beginning with: start.  The default start value is 100."
        self.start = start
        self.counter = -1

    def generate(self):
        "Increase serial number by 1 and return."
        self.counter += 1
        return self.counter + self.start

    def reset(self):
        "Reset serial number"
        self.counter = -1

    
