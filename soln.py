class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if (l2 := len(s)) < (l1 := len(p)) or s=='' or p =='': return False

        p_hash = sum(map(hash, p))
        s_hash = sum(hash(s[i]) for i in range(l1))
        
        if p_hash == s_hash:
            return True
        else:
            for i in range(l2-l1):
                if p_hash == (s_hash := s_hash - hash(s[i]) + hash(s[i+l1])):
                    return True
        return False