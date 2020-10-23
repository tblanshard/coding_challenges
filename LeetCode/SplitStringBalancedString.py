class Solution:
    def balancedStringSplit(self, s: str) -> int:
#        totalCount = 0
#        i = 0
#        while i < len(s) - 1:
#            RorL = s[i]
#            countLetter = 0
#            while s[i] == RorL:
#                i+=1
#                countLetter+=1
#            newLetter = s[i]
#            for count in range(countLetter):
#                if s[i] == newLetter:
#                    i+=1
#                else:
#                    break
#            totalCount += 1
#        return totalCount

        totalCount = 0
        i = 0
        firstChar = s[i]
        firstCharCount = 1
        secondCharCount = 0
        while i < len(s) - 1:
            while (firstCharCount != secondCharCount) and (i < len(s) - 1):
                i += 1
                if s[i] == firstChar:
                    firstCharCount += 1
                else:
                    secondCharCount += 1
            totalCount += 1
            if i != len(s) - 1:
                firstChar = s[i+1]
                firstCharCount = 1
                secondCharCount = 0
                i += 1
        return totalCount
        
# need to improve time complexity
