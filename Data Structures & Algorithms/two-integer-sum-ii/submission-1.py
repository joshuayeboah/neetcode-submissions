class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1


        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum < target:
                left +=1

            if curSum > target:
                right -= 1
            if curSum == target:
                return [left+1, right+1]

        return


















        # l = 0
        # r = len(numbers) - 1

        # while l < r:
        #     curSum = numbers[l] + numbers[r]

        #     if curSum < target:
        #         l += 1
        #     elif curSum > target:
        #         r -= 1
        #     else:
        #         return [l +1, r+1]

        # return


        