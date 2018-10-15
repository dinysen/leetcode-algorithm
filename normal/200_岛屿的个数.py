class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or not grid:
            return 0;
        count = 0;
        row_size = len(grid);
        col_size = len(grid[0]);
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j,row_size,col_size);
                    count += 1;
        return count;
        
        
    def dfs(self,grid,i,j,row,col):
        if grid[i][j] == "1":
            grid[i][j] = "0";
            if i - 1 >= 0 :
                self.dfs(grid,i-1,j,row,col);
            if i + 1 <= row-1:
                self.dfs(grid,i+1,j,row,col);
            if j - 1 >= 0:
                self.dfs(grid,i,j-1,row,col);
            if j + 1 <= col-1:
                self.dfs(grid,i,j+1,row,col);
        return;