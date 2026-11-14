class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        for ch in s:
            if ch in dict_s:
                dict_s[ch]+=1
            else: 
                dict_s[ch]=1   
            
        print(dict_s)    

        dict_t={}
        for char in t:
            if char in dict_t:
                dict_t[char]+=1
            else:
                dict_t[char]=1

        print(dict_t)
            
        if dict_t==dict_s:
            return True
        return False        
