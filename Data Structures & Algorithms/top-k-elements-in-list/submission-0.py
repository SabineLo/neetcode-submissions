class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {} #key: num value: freq
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countNum[num] = 1 + countNum.get(num, 0)
        for num, count in countNum.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): #starting at highest, ending at lowest, going down by 1.
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



