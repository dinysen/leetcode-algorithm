class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = [];
        self.mins = [];

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x);
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x);
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.mins) > 0 and self.mins[-1] == self.nums[-1]:
            self.mins.pop();
        self.nums.pop();
        

    def top(self):
        """
        :rtype: int
        """
        return None if len(self.nums) == 0 else self.nums[-1];
        

    def getMin(self):
        """
        :rtype: int
        """
        return None if len(self.mins) == 0 else self.mins[-1];
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()