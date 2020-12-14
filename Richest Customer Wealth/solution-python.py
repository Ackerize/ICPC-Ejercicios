class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            sumAccounts = 0
            for j in range(len(accounts[i])):
                sumAccounts += accounts[i][j]
            maxWealth = max(maxWealth, sumAccounts)
        return maxWealth