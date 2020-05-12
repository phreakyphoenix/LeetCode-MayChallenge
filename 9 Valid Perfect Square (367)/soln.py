class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num<2) or num in set([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]):
            return True
        
        left, right = 17, num >> 4
        while left <= right:
            mid = (left + right) >> 1
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False