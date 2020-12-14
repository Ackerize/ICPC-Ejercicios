class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        vector<int> result{nums.at(0)};
        for (int i = 0; i < nums.size() - 1; i++)
        {
            result.push_back(result.at(i) + nums.at(i + 1));
        }
        return result;
    }
};