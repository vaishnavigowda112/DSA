class Solution: 
    def longestCommonPrefix(self, strs: list[str]) -> str: 
        common_letters = "" 
        for i in range(len(strs[0])): 
            for char in strs: 
                if i >= len(char) or char[i] != strs[0][i]: 
                    return common_letters 
            common_letters += strs[0][i] 
        return common_letters