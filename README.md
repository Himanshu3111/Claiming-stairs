class Solution(object):
   def climb_stairs(n: int) -> int:
        if n <= 2:
            return n  

       prev2, prev1 = 1, 2 
       for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2

        return prev1
    
for i in range(1, 8):
    print(i, climb_stairs(i))
