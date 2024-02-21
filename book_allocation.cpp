#include <iostream>
#include <vector>
using namespace std;

bool isPossible(vector<int> arr, int n, int m, int mid)
{
    int studentCount = 1;
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (sum + arr[i] <= mid)
        {
            sum += arr[i];
        }
        else
        {
            studentCount++;
            if (studentCount > m || arr[i] > mid)
            {
                return false;
            }
            sum = arr[i];
        }
        if (studentCount > m)
        {
            return false;
        }
    }
    return true;
}

int BookAllocation(vector<int> arr, int n, int m)
{
    int start = 0;
    int ans = -1;
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr[i];

    int end = sum;
    while (start <= end)
    {
        int mid = start + (end - start) / 2;
        if (isPossible(arr, n, m, mid))
        {
            ans = mid;
            end = mid - 1;
        }

        else
        {
            start = end + 1;
        }
    }
    return ans;
}
