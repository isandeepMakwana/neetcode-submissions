class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):

            row_flags = [False] * 10
            col_flags = [False] * 10
            box_flags = [False] * 10

            for j in range(9):
                # Row Check
                if board[i][j] != ".":
                    num = int(board[i][j])

                    if row_flags[num]:
                        return False

                    row_flags[num] = True

                # Column Check
                if board[j][i] != ".":
                    num = int(board[j][i])

                    if col_flags[num]:
                        return False

                    col_flags[num] = True

                # Box Check
                row = (i // 3) * 3 + (j // 3)
                col = (i % 3) * 3 + (j % 3)

                if board[row][col] != ".":
                    num = int(board[row][col])

                    if box_flags[num]:
                        return False

                    box_flags[num] = True

        return True