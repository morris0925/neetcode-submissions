class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dic = {}
        # horizontal
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    dic[board[i][j]] = dic.get(board[i][j],0) + 1
                    if dic[board[i][j]] > 1:
                        return False
            dic = {}
        
        # vertical
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    dic[board[j][i]] = dic.get(board[j][i],0) + 1
                    if dic[board[j][i]] > 1:
                        return False
            dic = {}

        #square
        #which square
        for h in range(3):
            for v in range(3):
                #inside square
                for i in range(3):
                    for j in range(3):
                        if board[3*h+i][3*v+j] != '.':
                            dic[board[3*h+i][3*v+j]] = dic.get(board[3*h+i][3*v+j],0) + 1
                            if dic[board[3*h+i][3*v+j]] > 1:
                                return False
                dic = {}

        return True


    




        