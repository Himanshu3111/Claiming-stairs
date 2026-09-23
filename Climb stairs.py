class Solution(object):
    @staticmethod
    def climb_stairs(n: int) -> int:
        if n <= 2:
            return n  # ways(1) = 1, ways(2) = 2

        prev2, prev1 = 1, 2  # ways(1), ways(2)
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1


# quick test
for i in range(1, 8):
    print(i, Solution.climb_stairs(i))