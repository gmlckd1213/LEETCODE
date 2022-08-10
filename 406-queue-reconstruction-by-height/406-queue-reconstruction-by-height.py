class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key=lambda p: (-p[0], p[1]))
        # res = []
        # for p in people:
        #     res.insert(p[1], p)
        # return res
        
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0],person[1]))#최대힙활용 - 
            
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
    
        #시간복잡도 O(n+log(n))