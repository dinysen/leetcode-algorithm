class MyCircularQueue:

    def __init__(self, k):
        self.queue = [None for i in range(k)];
        self.s = -1;
        self.e = -1;
        

    def enQueue(self, value):
        if self.e == -1 and self.s == -1:
            self.e = 0;
            self.s = 0;
            self.queue[self.e] = value;
            return True;
        
        next_e = 0 if self.e == len(self.queue)-1 else self.e + 1;
        if next_e == self.s:
            return False;
        else:
            self.queue[next_e] = value;
            self.e = next_e;
            return True;
        

    def deQueue(self):
        if self.e == -1 and self.s == -1:
            return False;
        
        next_s = 0 if self.s + 1 > len(self.queue)-1 else self.s + 1;
        self.queue[self.s] = None;
        if self.e == self.s:
            self.e = -1;
            self.s = -1;
            return True;
        else:
            self.s = next_s;
            return True;
        

    def Front(self):
        if self.s == -1:
            return -1;
        return self.queue[self.s];
        

    def Rear(self):
        if self.e == -1:
            return -1;
        return self.queue[self.e];
        

    def isEmpty(self):
        return self.s == -1 and self.e == -1;
        

    def isFull(self):
        next_e = 0 if self.e == len(self.queue)-1 else self.e + 1;
        return next_e == self.s;
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()