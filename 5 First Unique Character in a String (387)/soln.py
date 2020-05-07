from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for element in c.elements():
            if(c[element]==1):
                return s.index(element)
        return -1
