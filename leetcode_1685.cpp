class Solution
{
public:
    vector<int> getSumAbsoluteDifferences(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> result(n, 0);

        int prefixSum = 0;
        int suffixSum = 0;

        // Calculate suffix sum
        for (int i = 0; i < n; ++i)
        {
            suffixSum += nums[i];
        }

        // Calculate the result based on prefix sum and suffix sum
        for (int i = 0; i < n; ++i)
        {
            result[i] = i * nums[i] - prefixSum + suffixSum - (n - i) * nums[i];
            prefixSum += nums[i];
            suffixSum -= nums[i];
        }

        return result;
    }
};