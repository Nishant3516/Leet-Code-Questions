class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        frequencyOfChars = {}
        frequencyInString = {}

        # Count the frequency of each character in target
        for char in target:
            if char not in frequencyOfChars:
                frequencyOfChars[char] = 1
            else:
                frequencyOfChars[char] += 1

        # Count the frequency of each character in the input string s
        for char in s:
            if char not in frequencyInString:
                frequencyInString[char] = 1
            else:
                frequencyInString[char] += 1

        result = float('inf')

        for char, count in frequencyOfChars.items():
            if char not in frequencyInString:
                return 0
            result = min(result, frequencyInString[char] // count)

        return result
