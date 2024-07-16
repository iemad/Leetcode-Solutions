class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}

        for i in range(len(s)):
            # For string s
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
            
            # For string t
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1

        return dict_s == dict_t
        
