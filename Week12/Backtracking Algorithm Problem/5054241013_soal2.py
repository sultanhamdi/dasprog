class Solution(object):
    def combine(self, n, k):
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
        
        backtrack(1)
        return res