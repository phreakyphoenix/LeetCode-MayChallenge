from collections import Counter
class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        if s == '' or p == '' or lp>ls: return []      

        s = [ord(ch) for ch in s]
        p = [ord(ch) for ch in p]

        rp = []                             #region proposal
        sum_p = sum(p)       
        sum_s = sum(s[0:lp])
        
        if sum_s == sum_p:
            rp.append(0)

        lim = ls - lp
        for i in range(0, lim):
            sum_s = sum_s -s[i] +s[i+lp]
            if sum_s == sum_p:
                rp.append(i+1)
        if rp==[]:
            return []
        
        l=[]
        counter_p = Counter(p)
        for i in rp:
            counter_s = Counter(s[i:i+lp])
            if counter_s == counter_p:
                l.append(i)
        return l