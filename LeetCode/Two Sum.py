class Solution:
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy_array = nums[:]
        for i, number in enumerate(nums):
            others = nums[(i+1):len(nums)]
            remainder = target - number
            if remainder in others:
                first_index = copy_array.index(number);
                nums[first_index] = "a"
                return [first_index, nums.index(remainder)]
