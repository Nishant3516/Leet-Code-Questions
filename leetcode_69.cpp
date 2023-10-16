class Solution
{
public:
    long long int mySqrt(int num)
    {
        if (num <= 1)
            return num;

        int start = 1;
        int end = num - 1;
        long long int ans = -1;
        while (start <= end)
        {
            long long int mid = start + (end - start) / 2;
            if (mid * mid == num)
            {
                return mid;
            }
            if (mid * mid > num)
            {
                end = mid - 1;
            }
            else
            {
                ans = mid;
                start = mid + 1;
            }
        }
        return ans;
    }
};