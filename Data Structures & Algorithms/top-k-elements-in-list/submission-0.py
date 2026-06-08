class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter


        freq_list = Counter(nums)

        heap = []

        for num in freq_list.keys():
            heapq.heappush(heap, (freq_list[num], num))
            if len(heap) > k:
                heapq.heappop(heap)


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res



        