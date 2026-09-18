class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {} # key: nums value: freq
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            res[num] = 1 + res.get(num, 0)
        for key, value in res.items(): #remember the res.items in order to reverse
            bucket[value].append(key)

        output = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output 

        


