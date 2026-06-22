class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            sorted_alphabet = "".join(sorted(word))
            if sorted_alphabet not in dic:
                dic[sorted_alphabet] = []
                dic[sorted_alphabet].append(word)
            else:
                dic[sorted_alphabet].append(word)
        
        output = []
        for sorted_alphabet in dic:
            output.append(dic[sorted_alphabet])
        
        return output


            

        