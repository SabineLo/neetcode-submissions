class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strLen = 0
        if len(word1) > len(word2):
            strLen = len(word1)
        else:
            strLen = len(word2)
        newWord = []
        for i in range(strLen):
            if i < len(word1):
                newWord.append(word1[i]) #wrong because of out of range so 
            if i < len(word2):
                newWord.append(word2[i])
        return "".join(newWord)
