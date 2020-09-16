class Solution:
    def defangIPaddr(self, address: str) -> str:
        #FIRST ATTEMPT
        #return address.replace(".","[.]")
        split = list(address)
        for i,c in enumerate(split):
            if c == ".":
                split[i] = "[.]"
        return "".join(split)
        
# current code stats
# Runtime: 24 ms, faster than 93.31% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.8 MB, less than 50.47% of Python3 online submissions for Defanging an IP Address.
