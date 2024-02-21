class Solution:
    def largestGoodInteger(self, num: str) -> str:
        size = 3

        largest = ""
        current_window = num[:size]

        for x in range(size, len(num)):
            if current_window[0] == current_window[1] == current_window[2]:
                largest = max(largest, current_window)

            if largest == "999":
                return largest

            # Update the window by removing the first character and adding the next one
            current_window = current_window[1:] + num[x]

        # Check the last window after the loop
        if current_window[0] == current_window[1] == current_window[2]:
            largest = max(largest, current_window)

        return largest
