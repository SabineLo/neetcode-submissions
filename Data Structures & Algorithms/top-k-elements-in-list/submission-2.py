class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            freqCount[num] = 1 + freqCount.get(num, 0)
        for num, count in freqCount.items():#items -> key, value because goal is to swap    
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        


