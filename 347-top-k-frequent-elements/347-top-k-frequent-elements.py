class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums).most_common()
        answer = []
        for i in range(k):
            answer.append(freqs[i][0])


                
        return answer