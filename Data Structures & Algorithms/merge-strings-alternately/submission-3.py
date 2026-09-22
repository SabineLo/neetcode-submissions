class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wordLen1 = len(word1)
        wordLen2 = len(word2)
        newWord = []
        for i in range(max(wordLen1,wordLen2)):
            if i < wordLen1:
                newWord.append(word1[i])
            if i < wordLen2:
                newWord.append(word2[i])
        return "".join(newWord)
