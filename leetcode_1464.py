class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        max1_index = nums.index(max1)
        nums[max1_index] = float('-inf')
        max2 = max(nums)

        return (max1-1)*(max2-1)
