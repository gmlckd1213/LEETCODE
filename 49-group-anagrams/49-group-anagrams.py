class Solution:
                
        
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
    
    
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     h = {}
    #     for word in strs:
    #         sortedWord = ''.join(sorted(word))
    #         if sortedWord not in h:
    #             h[sortedWord] = [word]
    #         else:
    #             h[sortedWord].append(word)
    #     final = []
    #     for value in h.values():
    #         final.append(value)
    #     return final
