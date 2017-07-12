class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        length = len(self.minstack)
        if length == 0:
            self.minstack.append(x)
        else:
            low = 0
            high = length - 1
            if x <= self.minstack[low]:
                self.minstack.insert(0,x)
            elif x >= self.minstack[high]:
                self.minstack.append(x)
            else:
                self.binarySearch(low,high,x)


    def binarySearch(self, low, high, x):
        if high-low <= 1:
            self.minstack.insert(high,x)
            return
        mid = (low + high)/2
        if self.minstack[mid]<x:
            self.binarySearch(mid,high,x)
        else:
            self.binarySearch(low,mid,x)

    def pop(self):
        """
        :rtype: void
        """
        self.minstack.remove(self.stack.pop())

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
