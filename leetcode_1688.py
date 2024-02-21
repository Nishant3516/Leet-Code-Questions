class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 0:
            if n & 1 == 0:
                res = n // 2
                n = res
                matches += res
            else:
                if n == 1:
                    return matches
                res = (n - 1) // 2
                n = res + 1
                matches += res
        return matches
