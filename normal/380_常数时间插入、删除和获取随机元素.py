import random;
class RandomizedSet:

    def __init__(self):
        self.d = {};
        self.l = [];

    def insert(self, val):
        if not val in self.d:
            self.l.append(val);
            self.d[val] = len(self.l)-1;
            return True;
        return False;
        

    def remove(self, val):
        if not val in self.d:
            return False;
        pos = self.d[val];
        last = self.l[-1];
        self.d[last] = pos;
        self.l[pos] = last;
        self.d.pop(val);
        self.l.pop();
        return True;
        

    def getRandom(self):
        return self.l[random.randint(0,len(self.l)-1)];
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()