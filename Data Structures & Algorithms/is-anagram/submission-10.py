class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dictionary 
        if len(s) != len(t):
            return False

        letterCountS = {}
        letterCountT = {}

#for dictionary get 
        for i in range(len(s)):
            letterCountS[s[i]] = 1 + letterCountS.get(s[i], 0) #defaultdict basically 0
            letterCountT[t[i]] = 1 + letterCountT.get(t[i], 0)
        return letterCountS == letterCountT