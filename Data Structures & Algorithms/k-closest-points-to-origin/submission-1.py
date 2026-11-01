class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        disPoints = []
        for p in points:
            dis = math.sqrt(p[0]**2 +  p[1]**2)
            disPoints.append([dis, p[0], p[1]])
        
        heapq.heapify(disPoints)
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(disPoints)
            res.append([x, y])
        
        return res