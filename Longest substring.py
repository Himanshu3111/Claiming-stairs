class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()       # letters currently inside our window
        left = 0            # left edge of the window
        max_length = 0

        for right in range(len(s)):
            # if this letter is already in the window, shrink from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            # window size right now is (right - left + 1)
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length
