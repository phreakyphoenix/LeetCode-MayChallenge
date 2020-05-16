def kadane(a): 
    n = len(a) 
    global_max = a[0]
    curr_max = a[0]
    for i in range(1, n): 
        curr_max = max(curr_max + a[i] , a[i])
        if (global_max < curr_max): 
            global_max = curr_max 
    return global_max 

class Solution:
    def maxSubarraySumCircular(self,a: List[int]) -> int:
        n = len(a) 
        all_neg = True
        for e in a:
            if e>0:
                all_neg = False
                break
        if all_neg:
            return max(a)
        
        k_plus = kadane(a)
        k_minus= kadane([-e for e in a])
        return max(sum(a)+k_minus, k_plus)