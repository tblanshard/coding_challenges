import functools

class Solution:
    
    def subtractProductAndSum(self, n: int) -> int:
        #ATTEMPT 1
        #splitDigits = list(str(n))
        #return abs((functools.reduce(lambda a,b : int(a)+int(b), splitDigits) - functools.reduce(lambda a,b : int(a)*int(b), splitDigits)))
        
        #ATTEMPT 2 - uses less memory than 99.24% of submissions
        #splitDigits = list(str(n))
        #sumDigits = 0
        #productDigits = 1
        #for n in splitDigits:
        #    sumDigits += int(n)
        #    productDigits *= int(n)
        #return productDigits - sumDigits
        
        #ATTEMPT 3
        totals = {"sumDigits":0, "productDigits":1}
        for d in list(str(n)):
            totals["sumDigits"] += int(d)
            totals["productDigits"] *= int(d)
        return totals["productDigits"] - totals["sumDigits"]
