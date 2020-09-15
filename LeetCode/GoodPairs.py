class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        #FIRST SOLUTION
 #       for i,x in enumerate(nums):
  #          for j,y in enumerate(nums):
   #             if (nums[i] == nums[j] and i < j):
    #                count+=1
    
        #for i,x in enumerate(nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                #if (x == nums[j] and i < j):
                if (nums[i] == nums[j] and i < j):
                    count+=1
        return count

    
    #current code stats:
    #Runtime: 28 ms, faster than 91.27% of Python3 online submissions for Number of Good Pairs.
    #Memory Usage: 13.9 MB, less than 41.71% of Python3 online submissions for Number of Good Pairs.
