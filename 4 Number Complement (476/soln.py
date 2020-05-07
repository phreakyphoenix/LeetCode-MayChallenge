class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num == 0:
            return 1
        return num^(2**(int(math.log2(num)) + 1) -1)
