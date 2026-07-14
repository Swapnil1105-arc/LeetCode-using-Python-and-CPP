class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        alpha="qwertyuiopasdfghjklzxcvbnm1234567890"
        for i in s.lower():
            if i in alpha :
                n+=i
            else:
                pass
        if n==n[::-1]:
            return True
        else:
            return False
