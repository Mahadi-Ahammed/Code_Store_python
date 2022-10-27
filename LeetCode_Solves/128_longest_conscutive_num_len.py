class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        maxLen = 0
        for i in numSet: #removes double number and improves loop
            currnLen=0
            if i-1 not in numSet: #if it is the lowest number in the sequency then start count the len
                while i+currnLen in numSet: #cheks if next num in len or continue.
                    currnLen +=1
                maxLen= max(maxLen,currnLen)
        return maxLen
                
