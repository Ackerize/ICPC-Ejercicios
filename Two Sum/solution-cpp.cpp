class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {
                if (i != j && nums.at(i) + nums.at(j) == target)
                {
                    if (i < j)
                        return {i, j};
                    return {j, i};
                }
            }
        }
        return {0, 1};
    }
};