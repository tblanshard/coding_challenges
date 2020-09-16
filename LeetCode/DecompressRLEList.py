class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #ATTEMPT 1
        #output = []
        #for i in range(0, len(nums), 2):
        #    output = output + [nums[i+1]]*nums[i]
        #return output
    
        #ATTEMPT 2
        count = nums[::2]
        toDuplicate = (nums[1:len(nums)])[::2]
        result = []
        for i in range(len(nums[::2])):
            result = result + [toDuplicate[i]]*count[i]
        return result
        
 # need to improve space and time complexity
