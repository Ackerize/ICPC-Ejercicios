class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        rightSide = nums[:n]
        leftSide = nums[n:]
        result = []
        for i in range(n):
            result.append(rightSide[i])
            result.append(leftSide[i])
        return result