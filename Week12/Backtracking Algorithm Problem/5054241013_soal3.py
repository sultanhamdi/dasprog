class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiagonal = set()  # (r + c)
        negdiagonal = set()  # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posdiagonal or (r - c) in negdiagonal:
                    continue
                
                col.add(c)
                posdiagonal.add(r + c)
                negdiagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posdiagonal.remove(r + c)
                negdiagonal.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
