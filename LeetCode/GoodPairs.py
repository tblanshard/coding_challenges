class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        #FIRST SOLUTION
 #       for i,x in enumerate(nums):
  #          for j,y in enumerate(nums):
   #             if (nums[i] == nums[j] and i < j):
    #                count+=1
    
        for i,x in enumerate(nums):
            for j in range(i, len(nums)):
                if (x == nums[j] and i < j):
                    count+=1
        return count
