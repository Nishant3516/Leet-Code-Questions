class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        frequencyOfChars = {}
        mainList = []

        # Count the frequency of each character in chars
        for char in chars:
            if char not in frequencyOfChars:
                frequencyOfChars[char] = 1
            else:
                frequencyOfChars[char] += 1

        # Check if each word in words can be formed from chars
        for word in words:
            frequencyOfIndChar = frequencyOfChars.copy()  # Create a copy for each word
            for char in word:
                if char not in frequencyOfIndChar or frequencyOfIndChar[char] == 0:
                    break
                frequencyOfIndChar[char] -= 1
            else:
                mainList.append(word)

        # Calculate the total length of words in mainList
        totalLength = sum(len(word) for word in mainList)

        return totalLength