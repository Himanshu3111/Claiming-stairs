class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = [1, 2]
        for i in range(2, n):
            a.append(a[i-2] + a[i-1])

        return a[-1]
