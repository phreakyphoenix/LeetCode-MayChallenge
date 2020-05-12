from collections import defaultdict

class Solution(object):
    def findJudge(self, N, trust):
        if N==1:
            return 1
        if N==2 and len(trust)==1:
            return trust[0][1]
        if len(trust) < N-1:
            return -1
        
        truster = defaultdict(int)
        trustee = defaultdict(int)
        
        for (p1, p2) in trust:
            truster[p1] += 1
            trustee[p2] += 1
        
        for judge, trusted_by in trustee.items():
            if trusted_by == N-1 and judge not in truster.keys():
                return judge    
        return -1