'''
执行用时：84 ms
'''
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dchar1 = {}
        dchar2 = {}
        
        for c1 in s:
            if c1 in dchar1:
                dchar1[c1] = dchar1[c1] + 1
            else:
                dchar1[c1] = 1
                
        for c2 in t:
            if c2 in dchar2:
                dchar2[c2] = dchar2[c2] + 1
            else:
                dchar2[c2] = 1
                
        return dchar1 == dchar2