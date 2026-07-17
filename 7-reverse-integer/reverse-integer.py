class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        n = 0
        if x < 0:
            x = x*-1
            n = 1
        arr = [int(i) for i in str(x)]
        arr.reverse()
        for i in range(len(arr)):
            r += arr[i] * (10**(len(arr)-i-1))
        if n == 1:
            r = r*-1
        if r > 2**31 or r < -(2**31):
            return(0)
        return(r)