class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longestSubstring=0
        sett=set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1

            sett.add(s[r])
            w=(r-l)+1
            longestSubstring=max(longestSubstring,w)
        return longestSubstring
