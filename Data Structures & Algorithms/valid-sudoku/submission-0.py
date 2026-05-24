class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check col
        for i in range(9):
            if not self.check_col(board, i):
                return False
        # check row
        for i in range(9):
            if not self.check_row(board, i):
                return False
        # check box
        for i in range(9):
            for j in range(9):
                if i % 3 == j % 3 == 0:
                    if not self.check_box(board, [i, j]):
                        return False
        return True
    
    def check_col(self, board, start):
        col_content = set()
        for i in range(9):
            if board[start][i] in col_content and board[start][i] != '.':
                return False
            col_content.add(board[start][i])
        return True

    def check_row(self, board, start):
        row_content = set()
        for i in range(9):
            if board[i][start] in row_content and board[i][start] != '.':
                return False
            row_content.add(board[i][start])
        return True

    def check_box(self, board, start):
        box_content = set()
        for i in range(start[0], start[0] + 3):
            for j in range(start[1], start[1] + 3):
                if board[i][j] in box_content and board[i][j] != '.':
                    return False
                box_content.add(board[i][j])
        return True