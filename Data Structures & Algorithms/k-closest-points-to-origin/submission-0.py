class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)

        for point in points:
            dist = point[0]**2 + point[1]**2

            heapq.heappush(arr , (abs(dist) , point))

        res=[]
        for a in range(k):
            
            res.append(heapq.heappop(arr)[1])

        return res