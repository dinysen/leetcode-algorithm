class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = "";
        l = 0;
        for ch in s:
            if ch not in res:
                res += ch;
            else:
                l = max(len(res),l);
                index = res.index(ch);
                res = res[index+1:]+ch;
        l = max(len(res),l);
        return l;
                    
            
-----------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans,i,j = 0,0,0;
        size = len(s);
        while j < size:
            if s[j] not in s[i:j]:
                j += 1;
                ans = max(j-i,ans);
            else:
                i += 1;
        return ans;
            

-----------------------------------------------------
#枚举法 LTE T.T
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0;
        visited = [];
        m = {};
        for i in s:
            for k,v in m.items():
                if v and i not in visited[k]:
                    visited[k].append(i);
                elif v and i in visited[k]:
                    m[k] = False;
            visited.append([i]);
            m[len(visited)-1] = True;
        return max(map(lambda x : len(x),visited));
                    