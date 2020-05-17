class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (l2 := len(s)) < (l1 := len(p)): return

        p_hash = sum(map(hash, p))
        s_hash = sum(hash(s[i]) for i in range(l1))
        
        if p_hash == s_hash:
            return [0] + list(i+1 for i in range(l2-l1) if p_hash==(s_hash:=s_hash-hash(s[i])+hash(s[i+l1])))
        else:
            return list(i+1 for i in range(l2-l1) if p_hash==(s_hash:=s_hash-hash(s[i])+hash(s[i+l1])))