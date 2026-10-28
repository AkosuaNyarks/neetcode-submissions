class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results=[]
        new_dict=defaultdict(list)
        for i in strs:
            word=tuple(sorted(i))
            new_dict[word].append(i)
        print(new_dict)
        for key,value in new_dict.items():
            results.append(value)
        return results

        