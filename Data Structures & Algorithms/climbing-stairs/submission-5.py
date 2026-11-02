class Solution:
    memoization = {1:1, 2:2, 3:3}
    def climbStairs(self, n: int) -> int:
        if n in self.memoization.keys():
            return self.memoization[n]
        self.memoization[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memoization[n]