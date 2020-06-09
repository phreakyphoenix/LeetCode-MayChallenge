class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [0]+A
        B = [0]+B
        len1 = len(A)
        len2 = len(B)
        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        for i in range(1,len1):
            for j in range(1,len2):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])                    
        return dp[-1][-1]  