# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in s and t
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1

        # All counts must return to zero
        return all(count == 0 for count in freq.values())





# ⏱ Complexity
# Time: O(n)
# Space: O(k) where k is the number of distinct Unicode characters


# What would NOT work for Unicode
# ❌ Fixed-size array approach
# count = [0] * 26  # only works for lowercase English letters
# Fails because:
#     Unicode has thousands of characters
#     No fixed or small alphabet size