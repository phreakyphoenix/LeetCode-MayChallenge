class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {k+1:set() for k in range(N)}
        for (truster, trustee) in trust:
            d[truster].add(trustee)
        
        trusts_no_one = [k for k,v in d.items() if len(v)==0]
        if len(trusts_no_one)!=1:
            return -1
        judge = trusts_no_one[0]
        del(d[judge])
        for trustees in d.values():
            if judge not in trustees:
                return -1
        return judge
        