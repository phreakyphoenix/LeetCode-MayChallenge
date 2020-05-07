from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return  Counter(nums).most_common(1)[0][0]
    
        # half_length = sum(c.values())/2
        # for e in c.elements():
        #     if c[e]>half_length:
        #         return e
        
        # return sorted(nums)[len(nums)//2]