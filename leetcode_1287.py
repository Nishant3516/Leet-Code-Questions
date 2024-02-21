class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Solution 1
        # n=len(arr)
        # percent25=n*0.25

        # counts={}
        # for i in arr:
        #     if i in counts:
        #         counts[i]+=1
        #     else:
        #         counts[i]=1

        # for key,value in counts.items():
        #     if value>percent25:
        #         return key

        # Solution 2: Using Sliding Window
        n = len(arr)
        quarter_length = n // 4

        for i in range(n - quarter_length):
            if arr[i] == arr[i + quarter_length]:
                return arr[i]
