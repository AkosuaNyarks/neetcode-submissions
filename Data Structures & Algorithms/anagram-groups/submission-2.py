from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a  dictionary
        anagram_dict=defaultdict(list)
        for word in strs:
            sorted_word="".join(sorted(word))
            anagram_dict[sorted_word].append(word)
        return anagram_dict.values()



        