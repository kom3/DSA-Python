# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if not s or not t:
            return ""

        # Frequency map of required characters (t)
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # Sliding window frequency map
        window = {}

        # Number of unique characters needed
        required = len(need)
        formed = 0

        left = 0
        min_len = float('inf')
        result = ""

        # Expand window with right pointer
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If frequency matches requirement, increment formed
            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink window when all required characters are formed
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                # If requirement breaks, reduce formed
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result






# ⏱️ Complexity
    # Time: O(n + m)
    # Space: O(n)




