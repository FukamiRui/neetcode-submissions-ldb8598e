class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        set_memo = set()
        left = 0

        for right in range(len(s)):
            
            while s[right] in set_memo:
                set_memo.remove(s[left])
                left += 1
            set_memo.add(s[right])
            res = max(res, right - left + 1)
            
            
            
        return res

        