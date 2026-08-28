class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        r = 0
        l = 0
        res = []
        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                 nums[q.pop()]
            
            if l <= r - k:
                l += 1
 
            if q and q[0] < l:
                q.popleft()
            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])

            r += 1


        return res