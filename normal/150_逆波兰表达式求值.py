class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [];
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                b = int(stack.pop());
                a = int(stack.pop());
                if i == "+":
                    stack.append(a+b);
                if i == "-":
                    stack.append(a-b);
                if i == "*":
                    stack.append(a*b);
                if i == "/":
                    stack.append(a/b);
            else:
                stack.append(int(i));
        return int(stack[0]);