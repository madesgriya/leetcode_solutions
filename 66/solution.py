class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # combining the long integer
        s = [str(i) for i in digits]
        res = int("".join(s))
        
        res1 = res + 1
        return [int(x) for x in str(res1)]