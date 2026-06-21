class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = defaultdict(set)
        col_duplicates = [set() for i in range(len(board))]
        for col in range(len(board)):
            row_duplicates = set()
            for row in range(len(board[col])):

                # skips empty slots
                if board[col][row] == ".":
                    continue

                # handles duplicates in each row
                if board[col][row] in row_duplicates:
                    return False
                row_duplicates.add(board[col][row])

                # handles duplicates in each column
                if board[col][row] in col_duplicates[row]: 
                    return False
                col_duplicates[row].add(board[col][row])

                # handles duplicates in each 3x3 box
                key = col // 3
                value = row // 3
                if board[col][row] in res[(key,value)]:
                    return False
                res[(key,value)].add(board[col][row])
        return True

            

