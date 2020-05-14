class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        while True: 
            length = len(nums)
            if length == 1:
                return nums[0]              
            mid = length>>1
            if mid%2:                               #if half has odd length
                if nums[mid-1]==nums[mid]:
                    nums = nums[mid+1:]
                elif (nums[mid]==nums[mid+1]):
                    nums = nums[:mid]  
                else:
                    return nums[mid]
            else:                                   #if half has odd length
                if nums[mid-1]==nums[mid]:
                    nums = nums[:mid-1]
                elif (nums[mid]==nums[mid+1]):
                    nums = nums[mid+2:]  
                else:
                    return nums[mid]
        # out=0
        # for num in nums:
        #     out^=num
        # return out