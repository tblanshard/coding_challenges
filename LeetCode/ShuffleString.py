class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # FIRST SOLUTION
        pairs = []
        for i in range(len(s)):
            pairs.append([indices[i],s[i]])
        pairs.sort()
        return "".join([b for [a,b] in pairs])
    
        # SECOND SOLUTION
        answer = ""
        for i in indices:
            answer += s[i]
        return answer
    
        # THIRD SOLUTION
        pairs = {}
        for i in range(len(s)):
            pairs[indices[i]] = s[i]
        return "".join([b for (a,b) in sorted(pairs)])
        
  # not an ideal solution yet
