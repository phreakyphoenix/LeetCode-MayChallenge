from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote)
        for k,v in count.items():
            if magazine.count(k) < v:
                return False   
        return True