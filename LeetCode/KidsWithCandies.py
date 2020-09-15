class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        solution = [False]*len(candies)
        maxCandies = max(candies)
        for i,number in enumerate(candies):
            if (number == maxCandies) or (number + extraCandies >= maxCandies):
                solution[i] = True
        return solution
