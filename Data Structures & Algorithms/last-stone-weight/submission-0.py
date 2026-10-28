import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if first < second:
                difference=first-second
                heapq.heappush(stones,difference)
        if len(stones)==1:
            return -stones[0]
        return 0