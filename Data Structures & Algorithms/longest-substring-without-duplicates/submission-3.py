class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) ==1:
            return 1
        start = s[0]
        long = 0
        for i in range(1,len(s)):
            while s[i] in start[:i]:
                j = 0
                start = start[j+1:]
            start += s[i]
            long = max(long,len(start))
        return long;