class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(len(nums) - 1):
            result.append(result[i] + nums[i+1])
        return result