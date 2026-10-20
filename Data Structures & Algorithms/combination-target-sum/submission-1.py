class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.curr = []

        def dfs(i, currSum):

            if target == currSum:
                self.res.append(self.curr.copy())
                return

            if i >= len(nums) or currSum > target:
                return
            

            
            self.curr.append(nums[i])
            dfs(i, currSum + nums[i])

            self.curr.pop()
            dfs(i + 1, currSum)

        
        dfs(0, 0)
        return self.res
            




        