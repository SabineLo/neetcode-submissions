class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s))) #so when i decode it knows how long it is supposed to be
            result.append("#") #why this? just to have a separator??
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #slicing j not included so i - j so i = 0 j is position of # so it gets me the number/ length of the word
            i = j + 1 #new starting positon word starts
            j = i + length #leads me to end of word to the number  
            result.append(s[i:j]) #the full word
            i = j # new number length
        return result
