class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check the length of both list.# if they aren't equal then it can't be an anagram
        if len(s)!=len(t):
            return False
        else:
            #use the sorted function 
            s_sorted=sorted(s)
            t_sorted=sorted(t)
            if s_sorted==t_sorted:
                return True
            else:
                return False


        