class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        map<int, int> frequencyMap;
        for (auto i : arr)
            frequencyMap[i]++;
        set<int> uniqueSet;
        for (auto i : frequencyMap)
            uniqueSet.insert(i.second);
        return frequencyMap.size() == uniqueSet.size();
    }
};