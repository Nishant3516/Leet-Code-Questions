class Solution:
    def largestOddNumber(self, string: str) -> str:
        if not string or (len(string) == 1 and int(string) % 2 == 1):
            return string

        # Find the rightmost odd digit
        for i in range(len(string) - 1, -1, -1):
            if int(string[i]) % 2 == 1:
                return string[: i + 1]

        return ""
