class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=dict()
        if len(s)!=len(t):
            return False

        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        print(count)
        for char in t:
            if char in count:
                count[char]-=1
            else:
                return False
        print(count)

        for char in t:
            if count[char]!=0:
                return False
        return True

     

        

        