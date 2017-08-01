class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashR = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        hashC = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        hashB = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if i in hashR[board[i][j]]:
                    return False
                else:
                    hashR[board[i][j]].append(i)
                if j in hashC[board[i][j]]:
                    return False
                else:
                    hashC[board[i][j]].append(j)
                x = i/3 * 3 + 1
                y = j/3 * 3 + 1
                if (x,y) in hashB[board[i][j]]:
                    return False
                else:
                    hashB[board[i][j]].append((x,y))
        return True
