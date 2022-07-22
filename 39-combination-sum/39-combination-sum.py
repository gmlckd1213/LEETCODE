class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        min_num = min(candidates)
        max_num = max(candidates)

        start = int(target / max_num)
        end = int(target / min_num)
        result = []

        for index in range(start, end + 1):
            for comb in itertools.combinations_with_replacement(candidates, index):
                if sum(comb) == target:
                    result.append((comb))

        return result