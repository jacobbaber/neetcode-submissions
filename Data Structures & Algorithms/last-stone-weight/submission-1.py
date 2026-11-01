class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            newStone = abs(x-y)
            if newStone == 0:
                continue
            heapq.heappush_max(stones, newStone)

        if len(stones) == 0:
            return 0
        return stones[0]