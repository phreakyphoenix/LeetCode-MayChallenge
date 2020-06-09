class Solution(object):
    def minDistance(self, A, B):
        A_len = len(A)
        B_len = len(B)

        tbl = [[0 for _ in range(B_len + 1)] for _ in range(A_len + 1)]

        for i in range(A_len + 1):
            tbl[i][0] = i
        for j in range(B_len + 1):
            tbl[0][j] = j

        for i in range(1, A_len + 1):
            for j in range(1, B_len + 1):
                if A[i - 1] == B[j - 1]:
                    tbl[i][j] = tbl[i - 1][j - 1]
                else:
                    tmp_insert = tbl[i][j - 1]
                    tmp_remove = tbl[i - 1][j]
                    tmp_replace = tbl[i - 1][j - 1]

                    tbl[i][j] = 1 + min(tmp_insert, tmp_remove, tmp_replace)

        return tbl[A_len][B_len]