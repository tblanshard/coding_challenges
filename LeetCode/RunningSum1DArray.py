import functools

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#        INITIAL SOLUTION
#        answer = []
#        for x in range(1,len(nums)+1):
#            answer.append(functools.reduce(lambda a,b : a+b, nums[0:x]))
#        return answer
        answer = [nums[0]]
        for x in range(1, len(nums)):
            answer.append(answer[x-1]+nums[x])
        return answer
        
