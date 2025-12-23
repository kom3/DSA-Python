# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


# Topics
#     Hash Table
#     Two Pointers
#     String
#     Sliding Window


# Pattern: Sliding window + Frequency Map


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Build frequency for s1 and first window of s2
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # Count initial matches
        matches = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right character
            r = ord(s2[right]) - ord('a')
            if freq2[r] == freq1[r]:
                matches -= 1
            freq2[r] += 1
            if freq2[r] == freq1[r]:
                matches += 1

            # remove left character
            l = ord(s2[left]) - ord('a')
            if freq2[l] == freq1[l]:
                matches -= 1
            freq2[l] -= 1
            if freq2[l] == freq1[l]:
                matches += 1

            left += 1

        return matches == 26








