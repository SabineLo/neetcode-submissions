class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        setS = defaultdict(int)
        setT = defaultdict(int)
        for i in range(len(s)):
            setS[s[i]] += 1
            setT[t[i]]+=1
        return setS == setT        