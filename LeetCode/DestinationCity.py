class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first = [pair[0] for pair in paths]
        second = [pair[1] for pair in paths]
        return list((set(second) - set(first)))[0]
            

# runtime - 44ms - 98.13% faster than Python3 submissions
# memory usage - 14.2 MB - less than 100% of Python3 submissions
