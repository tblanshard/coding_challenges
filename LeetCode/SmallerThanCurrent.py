class Solution:
    
    #def filterHelper(self, number, greaterThan):
    #    return (number < greaterThan)
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #ATTEMPT 1
        #answer = []
        #for i,n in enumerate(nums):
        #    copy = nums[:]
        #    copy.pop(i)
        #    answer.append(len(list(filter(lambda number: self.filterHelper(number,n), copy))))
        #return answer
    
        #ATTEMPT 2
        #result = [];
        #for number in nums:
        #    result.append([n < number for n in nums].count(True))
        #return result
        
        #ATTEMPT 3
        countLessThan = {}
        result = []
        sortedNums = sorted(nums)
        unique = sorted(set(nums), reverse=True)
        for i,number in enumerate(unique):
            countLessThan[number] = len(sortedNums[0:sortedNums.index(number)])
        for n in nums:
            result.append(countLessThan[n])
        return result
    
    # current solution stats
    # Runtime: 56 ms, faster than 84.77% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # Memory Usage: 13.9 MB, less than 38.44% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    
    # need to improve space complexity!
