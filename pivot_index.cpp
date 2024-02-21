#include <iostream>
#include <vector>
using namespace std;

int getPivot(vector<int> arr)
{
    int start = 0;
    int end = arr.size() - 1;
    while (start < end)
    {
        int mid = start + (end - start) / 2;
        if (arr[mid] >= arr[0])
        {
            start = mid + 1;
        }
        else
        {
            end = mid;
        }
        mid = start + (end - start) / 2;
    }
    return start;
}

int main()
{
    vector<int> arr = {7, 8, 1, 3, 5};
    int a = getPivot(arr);
    cout << a;
    return 0;
}