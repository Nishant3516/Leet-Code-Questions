class Solution
{
public:
    int reverse(int x)
    {
        int result = 0;
        while (x != 0)
        {
            int unit = x % 10;
            if ((result < INT_MIN / 10) || (result > INT_MAX / 10))
            {
                return 0;
            }
            result = (result * 10) + unit;
            x /= 10;
        }
        return result;
    }
};