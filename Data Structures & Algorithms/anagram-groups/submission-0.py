class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #The Goal of this program is to group all the anagrams together in a list of a list
        #{tuple(frequency/ how many "a-z" in a word), list(is the words with the same frequency/words)}
        anagram_dict = defaultdict(list) # And we do this to avoid a test case such as it start the dictionary with { key, []} a default value so no error
        #Its basically a default value for new keys
        for s in strs:
            count = [0] * 26 #basically making my key 26 characters then start off all 0
            for c in s:
                count[ord(c) - ord('a')] += 1 #I want to be able to match the letter I get with the correct index of the list
            anagram_dict[tuple(count)].append(s) #count is a list, and that cant be a list it has to be a tuple
        return list(anagram_dict.values())

