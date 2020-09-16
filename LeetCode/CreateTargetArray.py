class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [None]*len(nums)
        for i,element in enumerate(nums):
            if target[index[i]] == None:
                target[index[i]] = element
            else:
                target.insert(index[i],element)
        return [y for y in target if y != None]
        
 # REALLY slow
