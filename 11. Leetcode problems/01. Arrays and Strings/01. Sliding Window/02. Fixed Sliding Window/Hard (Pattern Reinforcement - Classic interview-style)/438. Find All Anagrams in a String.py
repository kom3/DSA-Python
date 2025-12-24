# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.




# Pattern: Fixed Sliding Window + Frequency map

# Solution 1 (using FREQUENCY MAPS)
from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # --------------------------------------------------
        # EDGE CASE:
        # If pattern is longer than the string,
        # no anagram window is possible.
        # --------------------------------------------------
        if len(s) < len(p):
            return []

        # --------------------------------------------------
        # FREQUENCY MAPS
        # freq1 -> frequency of characters in pattern p
        # freq2 -> frequency of characters in current window of s
        #
        # NOTE (IMPORTANT):
        # defaultdict(int) returns 0 for missing keys.
        # This means:
        #   - Accessing freq1[x] creates a key if x is missing
        #   - We MUST update match counts ONLY for characters in freq1
        #
        # If we used an array of size 26 instead:
        #   - No missing-key issue
        #   - No need for "char in freq1" checks
        # --------------------------------------------------
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        # --------------------------------------------------
        # Build frequency map for pattern p
        # --------------------------------------------------
        for char in p:
            freq1[char] += 1

        # --------------------------------------------------
        # Build frequency map for the first window of s
        # (window size == len(p))
        # --------------------------------------------------
        for i in range(len(p)):
            freq2[s[i]] += 1

        # --------------------------------------------------
        # total_matches:
        # Number of DISTINCT characters in p
        # whose frequencies currently match in the window
        # --------------------------------------------------
        total_matches = 0
        required_matches = len(freq1)
        result = []

        # --------------------------------------------------
        # Count initial matches
        # Only characters in freq1 matter
        # --------------------------------------------------
        for char in freq1:
            if freq1[char] == freq2[char]:
                total_matches += 1

        # --------------------------------------------------
        # SLIDING WINDOW
        # left  -> start index of window
        # right -> end index of window
        # --------------------------------------------------
        left = 0
        for right in range(len(p), len(s)):

            # If all required characters match, record index
            if total_matches == required_matches:
                result.append(left)

            # ---------------------------
            # ADD RIGHT CHARACTER
            # ---------------------------
            char = s[right]

            # If this character is part of p and was previously matching,
            # adding it will break the match
            if char in freq1 and freq2[char] == freq1[char]:
                total_matches -= 1

            # Add character to the window
            freq2[char] += 1

            # If after adding it matches again, restore match
            if char in freq1 and freq2[char] == freq1[char]:
                total_matches += 1

            # ---------------------------
            # REMOVE LEFT CHARACTER
            # ---------------------------
            char = s[left]

            # If this character is part of p and was matching,
            # removing it will break the match
            if char in freq1 and freq2[char] == freq1[char]:
                total_matches -= 1

            # Remove character from the window
            freq2[char] -= 1

            # If after removing it matches again, restore match
            if char in freq1 and freq2[char] == freq1[char]:
                total_matches += 1

            # Move window forward
            left += 1

        # --------------------------------------------------
        # Check the final window
        # --------------------------------------------------
        if total_matches == required_matches:
            result.append(left)

        return result


# Solution 2 (using FREQUENCY ARRAYS)
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # --------------------------------------------------
        # EDGE CASE:
        # If pattern p is longer than string s,
        # no anagram window is possible.
        # --------------------------------------------------
        if len(s) < len(p):
            return []

        # --------------------------------------------------
        # FREQUENCY ARRAYS (Fixed size: 26 for a–z)
        # freq1 -> frequency of characters in p
        # freq2 -> frequency of characters in current window of s
        #
        # IMPORTANT DIFFERENCE vs DICT:
        # - No missing keys
        # - No need to check "char in freq1"
        # - Every index [0..25] always exists
        # --------------------------------------------------
        freq1 = [0] * 26
        freq2 = [0] * 26

        # --------------------------------------------------
        # Build frequency array for pattern p
        # --------------------------------------------------
        for char in p:
            freq1[ord(char) - ord('a')] += 1

        # --------------------------------------------------
        # Build frequency array for the first window of s
        # (window size == len(p))
        # --------------------------------------------------
        for i in range(len(p)):
            freq2[ord(s[i]) - ord('a')] += 1

        # --------------------------------------------------
        # total_matches:
        # Number of characters (out of 26)
        # whose frequencies currently match
        # --------------------------------------------------
        total_matches = 0
        result = []

        # --------------------------------------------------
        # Count initial matches
        # --------------------------------------------------
        for i in range(26):
            if freq1[i] == freq2[i]:
                total_matches += 1

        # --------------------------------------------------
        # SLIDING WINDOW
        # left  -> start index of window
        # right -> end index of window
        # --------------------------------------------------
        left = 0
        for right in range(len(p), len(s)):

            # If all 26 characters match,
            # current window is an anagram
            if total_matches == 26:
                result.append(left)

            # ---------------------------
            # ADD RIGHT CHARACTER
            # ---------------------------
            idx = ord(s[right]) - ord('a')

            # If this character was previously matching,
            # adding it will break the match
            if freq2[idx] == freq1[idx]:
                total_matches -= 1

            # Add character to the window
            freq2[idx] += 1

            # If after adding it matches again,
            # restore the match
            if freq2[idx] == freq1[idx]:
                total_matches += 1

            # ---------------------------
            # REMOVE LEFT CHARACTER
            # ---------------------------
            idx = ord(s[left]) - ord('a')

            # If this character was previously matching,
            # removing it will break the match
            if freq2[idx] == freq1[idx]:
                total_matches -= 1

            # Remove character from the window
            freq2[idx] -= 1

            # If after removing it matches again,
            # restore the match
            if freq2[idx] == freq1[idx]:
                total_matches += 1

            # Move window forward
            left += 1

        # --------------------------------------------------
        # Check the final window
        # --------------------------------------------------
        if total_matches == 26:
            result.append(left)

        return result
