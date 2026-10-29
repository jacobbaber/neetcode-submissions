class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []


        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in nums:
                if n in perm:
                    continue
                perm.append(n)
                dfs()
                perm.pop()
        dfs()
        return res

            
 
            
            


        