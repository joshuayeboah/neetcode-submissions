class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap = {}


        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        # return    
  
        matchmap = dict()

        for i, num in enumerate(nums):
            diff = target - num

            if diff in matchmap:
                return [matchmap[diff], i]
            else:
                matchmap[num] = i

        return

       