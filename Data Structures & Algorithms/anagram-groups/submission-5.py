class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            key=tuple(count)
            new_dict[key].append(word)
        return list(new_dict.values())     