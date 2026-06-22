class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #還有標點符號要拿掉！
        s = "".join(c for c in s if self.alphaNum(c) is True) #拿掉空白與標點

        n = len(s)
        for i in range(int(n/2)):
            if s[i] == s[n-1-i]:
                continue
            else:
                return False
        return True

    def alphaNum(self, c):
        if ord(c) in range(ord('a'), ord('z')+1 ):  #mistake: put c instead of ord(c)
            # ord = ordinal(序號)
            # ord('z') +1 才包含到 'z'
            return True
        elif ord(c) in range(ord('0'), ord('9')+1 ):
            return True
        else:
            return False
        