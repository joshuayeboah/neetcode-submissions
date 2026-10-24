class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        ans = nums[0]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, n):
            candidates = (nums[i], nums[i]*dp_max[i-1], nums[i]*dp_min[i-1])

            dp_max[i] = max(candidates)
            dp_min[i] = min(candidates)

            ans = max(dp_max[i], ans)
            
        return ans

