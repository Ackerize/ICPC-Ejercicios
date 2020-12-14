class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximumCandies = max(candies)
        result = []
        for i in range(len(candies)):
            result.append(maximumCandies <= candies[i] + extraCandies)
        return result