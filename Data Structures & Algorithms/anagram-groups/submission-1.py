class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict={}
        # loop through each word in the list
        for s in strs:
            sorted_s="".join(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s]=[s]
            else:
                anagram_dict[sorted_s].append(s)
        return anagram_dict.values()
        
        