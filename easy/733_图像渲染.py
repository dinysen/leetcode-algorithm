class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.oldColor = image[sr][sc];
        self.newColor = newColor;
        self.width = len(image[0]);
        self.height = len(image);
        self.image = image;
        self.dfs(sr,sc);
        return self.image;
        
    def dfs(self,i,j):
        if self.image[i][j] == self.newColor or self.image[i][j] != self.oldColor:
            return;
        if self.image[i][j] == self.oldColor:
            self.image[i][j] = self.newColor;
        if i + 1 < self.height:
            self.dfs(i+1,j);
        if i - 1 >= 0:
            self.dfs(i-1,j);
        if j + 1 < self.width:
            self.dfs(i,j+1);
        if j - 1 >= 0:
            self.dfs(i,j-1);
        