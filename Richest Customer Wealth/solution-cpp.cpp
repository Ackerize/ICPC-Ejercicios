class Solution
{
public:
    int maximumWealth(vector<vector<int>> &accounts)
    {
        int maxWealth = 0;
        for (int i = 0; i < accounts.size(); i++)
        {
            int sumAccounts = 0;
            for (int j = 0; j < accounts.at(i).size(); j++)
            {
                sumAccounts += accounts.at(i).at(j);
            }
            maxWealth = max(maxWealth, sumAccounts);
        }
        return maxWealth;
    }
};