class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # key -> count : value -> word list

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) #we cant have a list as a key
            if key not in result: #must initalize if not exist
                result[key] = []
            result[key].append(word)
        return list(result.values()) #return values because it what we want

