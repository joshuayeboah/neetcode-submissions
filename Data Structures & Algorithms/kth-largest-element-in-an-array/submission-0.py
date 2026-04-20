class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        minHeap = nums

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return heapq.heappop(minHeap)

        


        