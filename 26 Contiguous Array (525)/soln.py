class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        hash_map = {}   
        curr_sum = 0 
        max_len = 0 
        ending_index = -1 
        for i in range (0, n):  
            curr_sum += -1 if(arr[i] == 0) else 1  
            if (curr_sum == 0):  
                max_len = i + 1 
                ending_index = i  
            if curr_sum in hash_map: 
                if max_len < i - hash_map[curr_sum]: 
                    max_len = i - hash_map[curr_sum] 
                    ending_index = i 
            else:  
                hash_map[curr_sum] = i   
        return max_len