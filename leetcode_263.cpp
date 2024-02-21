class Solution
{
public:
    bool isUgly(int n)
    {
        vector<int> factors;
        while (n % 2 == 0)
        {
            factors.push_back(2);
            n /= 2;
        }

        // Check for divisibility by odd numbers starting from 3
        for (int i = 3; i * i <= n; i += 2)
        {
            while (n % i == 0)
            {
                factors.push_back(i);
                n /= i;
            }
        }

        // If n is a prime number greater than 2
        if (n > 2)
        {
            factors.push_back(n);
        }
    }
};