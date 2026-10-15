class Solution:
    def hammingWeight(self, n: int) -> int:
        #so return how many 1s are in 23 as a bit
        res = 0
        while n: # while n  != 0
            n &= n - 1 #removes the rightmost bit awlaays n & n - 1= 24 - 23
            res += 1 # adds one because everytime one is removes
        return res