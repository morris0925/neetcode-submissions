class Solution:
    def encode(self, strs: List[str]) -> str: 
        encoded_string = ""
        for words in strs:
            encoded_string += str(len(words)) + "%"
            encoded_string += words
        return encoded_string

    def decode(self, s: str) -> List[str]: #AIM FOR BETTER TIME COMPLEXITY
        index = 0
        strs = []
        numInStr = ""
        while index < len(s):
            if s[index] != "%":
                numInStr += s[index]
                index += 1
                continue
            else: # when s[index] == "%":
                n = int(numInStr) #in case it's a two/three digit number
                numInStr = "" #set to blank
                
                word = ""
                index += 1 #go to the word
                word = s[index:index+n]
                    
                strs.append(word) 
                index += n
                continue
                
        
        return strs

            




