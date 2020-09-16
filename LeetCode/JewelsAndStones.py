class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
# ATTEMPT 1 - 44ms, 13.6MB
#        count = 0
#        for stone in S:
#            if stone in J:
#                count += 1
#        return count

# ATTEMPT 2 - 40ms, 13.8 MB
#        total = 0
#        stoneCount = {}
#        for stone in S:
#            if stone in stoneCount:
#                stoneCount[stone] += 1
#            else:
#                stoneCount[stone] = 1
#                
#        for count in stoneCount:
#            if count in J:
#                total += stoneCount[count]
#                
#        return total

# ATTEMPT 3 - 44ms, 13.6GB
#        count = 0
#        for stone in set(S):
#            if stone in J:
#                count += S.count(stone)
#        return count

# ATTEMPT 4 - 28ms, 13.8MB
            count = 0
            for jewel in J:
                if jewel in S:
                    count += S.count(jewel)
            return count
            
# current code stats
# Runtime: 28 ms, faster than 81.12% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14 MB, less than 48.58% of Python3 online submissions for Jewels and Stones.
