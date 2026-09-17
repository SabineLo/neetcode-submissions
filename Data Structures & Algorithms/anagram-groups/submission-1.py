class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
    #keys we are using count 
        for word in strs:
            count = [0] * 26
            for i in range(len(word)):
                count[ord(word[i]) - ord('a')] += 1

            anagrams[tuple(count)].append(word)

        return(list(anagrams.values()))
