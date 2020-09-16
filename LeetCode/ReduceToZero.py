class Solution:
    def numberOfSteps (self, num: int) -> int:
        # FIRST ATTEMPT
        count = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count

# needs work to find solution with smaller time and space complexity
