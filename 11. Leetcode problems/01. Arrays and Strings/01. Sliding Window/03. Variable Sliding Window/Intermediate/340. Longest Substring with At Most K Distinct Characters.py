# Problem Statement

# Given a string s and an integer k, find the length of the longest substring of s that contains at most k distinct characters.

# A substring is a contiguous sequence of characters within a string.

# Input

# A string s consisting of characters.

# An integer k representing the maximum number of distinct characters allowed in the substring.

# Output

# Return an integer representing the length of the longest substring that contains at most k distinct characters.

# Constraints

# 0 <= k <= s.length

# The string s may contain letters, digits, or symbols.

# Example 1

# Input:
# s = "eceba", k = 2

# Output:
# 3

# Explanation:
# The substring "ece" has at most 2 distinct characters (e and c) and has the maximum length.

# Example 2

# Input:
# s = "aa", k = 1

# Output:
# 2

# Explanation:
# The entire string "aa" contains only 1 distinct character.

# Notes

# If k = 0, the result should be 0 because no valid substring can contain zero distinct characters.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Edge case: if k is 0 or string is empty, no valid substring
        if k == 0 or not s:
            return 0

        # Dictionary to store character frequency in the current window
        window = {}

        left = 0          # Left pointer of the sliding window
        max_len = 0       # Stores the maximum valid window length found

        # Expand the window using the right pointer
        for right in range(len(s)):
            # Add current character to the window
            window[s[right]] = window.get(s[right], 0) + 1

            # If window becomes invalid (more than k distinct characters),
            # shrink it from the left until it becomes valid again
            while len(window) > k:
                window[s[left]] -= 1

                # Remove character from dictionary if its count becomes zero
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1  # Move left pointer forward

            # Update the maximum length of a valid window
            max_len = max(max_len, right - left + 1)

        return max_len






# ⏱ Complexity

# Time: O(n) — each character is visited at most twice

# Space: O(k) — stores at most k distinct characters