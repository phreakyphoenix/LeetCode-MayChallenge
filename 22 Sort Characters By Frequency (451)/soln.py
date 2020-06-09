class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s).most_common()
        s=''
        for tup in c:
            s+=tup[0]*tup[1]
        return s