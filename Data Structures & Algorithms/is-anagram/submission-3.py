class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        setS, setT= defaultdict(int), defaultdict(int)

#the reason im doing range(len(s)) is becuase if i only did
# for i in s I wouldnt be able to access t and compare the two
        for i in range(len(s)):
            setS[s[i]] += 1
            setT[t[i]] += 1
        return setS == setT

        