class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str=""
        for i in strs:
            new_str+=str(len(i))+"#"+i
        return new_str


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            if not s:
                return []
            j=i
            while s[j]!="#":
                #keep updating j
                j+=1
            #once j becomes equal to pound, we have the length of the str
            length=int(s[i:j])
            # print(length)
            k=j+1
            # Given the length of the  string we can now a up j to move through the string
            #Create an empty string
            word=s[k:k+length]
            res.append(word)
            i=k+length
        return res
        
