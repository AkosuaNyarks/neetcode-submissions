class Solution:

    def encode(self, strs: List[str]) -> str:
        newWord=""
        for word in strs:
            newWord+=str(len(word))+"#"+ word
        print(newWord)
        return newWord
        

    def decode(self, s: str) -> List[str]:
        res=[]
        l=0

        while l<len(s):
            r=l

            while r<len(s) and s[r]!="#" :
                r+=1

            length=int(s[l:r])
            word=s[r+1:length+1+r]
            res.append(word)
            l=length+1+r
            
        return res
        
        