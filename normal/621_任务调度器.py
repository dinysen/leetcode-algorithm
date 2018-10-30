class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l = [ 0 for i in range(26) ];
        for i in tasks:
            l[ord(i) - ord('A')] = l[ord(i)- ord('A')] + 1;
        
        l = sorted(l);
        
        count = 0;
        for i in l:
            if i == l[-1]:
                count +=1;
        
        return max(len(tasks),(l[-1]-1)*(n+1)+count);
        