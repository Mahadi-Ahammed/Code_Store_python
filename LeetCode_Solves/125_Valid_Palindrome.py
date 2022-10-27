class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        #make all lower and concate in a ans
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                #
                ans+=i
        if ans == ans[::-1]:
            return True
        return False
