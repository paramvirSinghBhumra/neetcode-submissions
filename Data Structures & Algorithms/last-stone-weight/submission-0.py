import heapq

class Solution:
    def reorder(self, stones):
        heapq.heapify(stones)
        max_heap = []

        while(len(stones) > 0):
            max_heap.append(heapq.heappop(stones))
        
        return max_heap

    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = self.reorder(stones)

        while(len(max_heap) > 1):
            x = max_heap.pop()
            y = max_heap.pop()

            if x != y:
                max_heap.append(abs(x-y))
                max_heap = self.reorder(max_heap)

        return 0 if len(max_heap) == 0 else max_heap.pop()
        