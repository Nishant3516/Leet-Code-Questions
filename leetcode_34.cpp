class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int first = binarySearch(nums, target, true);
        int last = binarySearch(nums, target, false);

        if (first > last)
        {
            // Element not found
            return {-1, -1};
        }
        else
        {
            return {first, last};
        }
    }

private:
    int binarySearch(vector<int> &nums, int target, bool findFirst)
    {
        int start = 0;
        int end = nums.size() - 1;
        int result = -1;

        while (start <= end)
        {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target)
            {
                result = mid;
                if (findFirst)
                {
                    end = mid - 1;
                }
                else
                {
                    start = mid + 1;
                }
            }
            else if (nums[mid] < target)
            {
                start = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }

        return result;
    }
};
