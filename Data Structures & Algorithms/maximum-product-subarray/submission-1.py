class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        ans = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, n):
            candidates = (nums[i], nums[i]*cur_max, nums[i]*cur_min)

            cur_max = max(candidates)
            cur_min = min(candidates)

            ans = max(cur_max, ans)
            
        return ans

