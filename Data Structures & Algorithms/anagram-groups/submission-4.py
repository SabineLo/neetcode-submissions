class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #count -> word

        #it would have 26 0's
        for s in strs:
            count = [0] * 26 #creating a list of 26 zeros
            for c in s:
            #finding the index based off of letter location 
                count[ord(c) - ord('a')] += 1
            key = tuple(count) #must turn into tuple because list cant be a key
            if key not in res: #initializing the key with a []
                res[key] = []
            res[key].append(s)
        return list(res.values()) #making sure value is returned as a list
            
