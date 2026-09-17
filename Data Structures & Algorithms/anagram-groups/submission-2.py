class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Key = (a,b,c) 
        #Value = (strings that have the same frequency as the key)
        group = defaultdict(list)
        for w in strs:
            alphabet = [0] * 26 #
            for c in w:
                alphabet[ord(c) - ord('a')] += 1
            group[tuple(alphabet)].append(w)

        return list(group.values())

