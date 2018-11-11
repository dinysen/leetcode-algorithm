#回溯---------------------------------------------
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return [];
        m = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        };
        self.size = len(digits);
        l = list(map(lambda x : m[x],digits));
        res = self.backtracking([],[],l);
        return res;
        
    def backtracking(self,res,tmp,digits):
        if len(tmp) == self.size:
            res.append("".join(tmp));
        
        if len(digits) == 0:
            return res;
            
        base = digits[0];
        for i in base:
            tmp.append(i);
            next_digit = digits[1:];
            self.backtracking(res,tmp,next_digit);
            tmp.pop();
        
        return res;
#-------------------------------------------------------------

from functools import reduce
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0 :
            return [];
        s = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        };
        d = {};
        digits_copy = [];
        for i in digits:
            if not i in d:
                digits_copy.append(i);
            else:
                d[i] = True;
        digits = digits_copy[:];
        temp = map(lambda x : s[x],digits);
        result = reduce(lambda x,y : [a+b for a in x for b in y],temp);
        return result;

#递归-------------------------------------------------
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return [];
        if len(digits) == 1:
            return list(m[digits]);
        res = [];
        tmp = self.letterCombinations(digits[1:]);
        for i in m[digits[0]]:
            for j in tmp:
                res.append(i+j);
        return res;