class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        

        res = []
        subset = []

        def dfs(i, cur):

            if cur == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or cur > target:
                return

            
            num = candidates[i]
            subset.append(candidates[i])
            
            dfs(i + 1, cur + num)

            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur)

        
        dfs(0,0)
        return res