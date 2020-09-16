class Solution:
    
    def filterHelper(self, number, greaterThan):
        return (number < greaterThan)
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i,n in enumerate(nums):
            copy = nums[:]
            copy.pop(i)
            answer.append(len(list(filter(lambda number: self.filterHelper(number,n), copy))))
        return answer
        
 #good space complexity
 #poor time complexity - needs work!
