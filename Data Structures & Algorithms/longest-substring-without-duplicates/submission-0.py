class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding window going over an area like im sliding lel while two pointer can be slidng but also from to front diff ways
        seen = set()
        #Sliding window im essentialy going to the right once I find a duplicate I go left and get rid of the left one cause I no longer
        #Need it since its repeated
        l = 0
        res = 0
        #Need left and right pointer
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        
            res = max(res, r - l + 1) #adding plus one I think because to make 1-index
        return res