class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0 or len(board) == 0:
            return False;
        self.board,self.word = board,word;
        self.row,self.col = len(board),len(board[0]);
        visited = [[False for i in range(self.col)] for j in range(self.row)];
        for i in range(self.row):
            for j in range(self.col):
                if self.exist_iter(0,i,j,visited):
                    return True;
        return False;
        
    def exist_iter(self,cur,i,j,visited):
        if cur == len(self.word):
            return True;
        
        if i < 0 or i >= self.row or j < 0 or j >= self.col or visited[i][j] or self.board[i][j] != self.word[cur]:
            return False;
        
        visited[i][j] = True;
        result =self.exist_iter(cur+1,i-1,j,visited) or\
                self.exist_iter(cur+1,i+1,j,visited) or\
                self.exist_iter(cur+1,i,j-1,visited) or\
                self.exist_iter(cur+1,i,j+1,visited);
        visited[i][j] = False;
        return result;