class Solution:
    def evalRPN(self, tokens):
        stack = [];
        countl = { 
            "+" : lambda x,y : x+y, 
            "-" : lambda x,y : x-y,
            "*" : lambda x,y : x*y,
            "/" : lambda x,y : x/y
        }
        for i in tokens:
            if i in countl:
                a = int(stack.pop());
                b = int(stack.pop());
                stack.append(countl[i](b,a));
            else:
                stack.append(i);
        return int(stack[-1]);