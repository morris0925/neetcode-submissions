class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #還有標點符號要拿掉！
        s = "".join(c for c in s if c.isalnum() is True) #拿掉空白與標點

        n = len(s)
        for i in range(int(n/2)):
            if s[i] == s[n-1-i]:
                continue
            else:
                return False
        return True

        