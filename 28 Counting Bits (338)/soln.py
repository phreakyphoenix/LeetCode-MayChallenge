class Solution:
    def countBits(self, num: int) -> List[int]:
        
        # return [bin(i).count('1') for i in range (num+1)]
        
        res=[0]
        while len(res)<=num:
            res+=[i+1 for i in res]
        return res[:num+1]
