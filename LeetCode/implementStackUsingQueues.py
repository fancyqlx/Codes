class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.L.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.L.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.L[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.L)==0:
            return True
        return False
