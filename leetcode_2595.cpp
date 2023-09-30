#include <iostream>
#include <vector>

class Solution
{
public:
    std::vector<int> evenOddBit(int n)
    {
        std::vector<int> result(2, 0);
        int bitPosition = 0;

        while (n > 0)
        {
            if ((n & 1) == 1)
            {
                result[bitPosition]++;
            }

            n >>= 1;          // Right shift to process the next bit.
            bitPosition ^= 1; // Toggle between 0 (even) and 1 (odd).
        }

        return result;
    }
};
