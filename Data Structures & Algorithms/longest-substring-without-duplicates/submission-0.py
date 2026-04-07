class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in new_set:
                new_set.remove(s[left])
                left += 1
            new_set.add(s[right])
            count = max(count, right - left +1)
        return count
            
     