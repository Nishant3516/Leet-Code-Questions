class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        possibleValues = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in possibleValues.values():
                stack.append(i)
            elif i in possibleValues.keys():
                if not stack or stack.pop() != possibleValues[i]:
                    return False
            else:
                return False

        return not stack
