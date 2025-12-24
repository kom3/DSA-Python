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


# Pattern: Fixed Sliding window + Frequency Map




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # APPROACH:
        # Fixed-size sliding window + frequency comparison
        # Window size = len(s1)
        # If any window in s2 has the same character frequencies as s1,
        # then s2 contains a permutation of s1.

        # EDGE CASE:
        # If s1 is longer than s2, no permutation is possible
        if len(s1) > len(s2):
            return False

        # Frequency arrays for lowercase English letters (a–z)
        # freq1 -> frequency of characters in s1
        # freq2 -> frequency of characters in the current window of s2
        # can also use a "defaultdict"; collections import defaultdict
        freq1 = [0] * 26
        freq2 = [0] * 26

        # total_matches keeps track of how many characters (out of 26)
        # have matching frequencies between freq1 and freq2
        # counter variable has a advantage over direct array comparision as in the later point of time only two element's frequency
        # going to be changing not the whole array of element's frequency, so this way we can minimise the computation cost
        total_matches = 0

        # Left pointer of the sliding window
        left = 0

        # STEP 1: Build initial frequency maps
        # - freq1 for s1
        # - freq2 for the first window of s2 (same length as s1)
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # STEP 2: Count how many characters already match in frequency
        # If all 26 match, we already found a valid permutation
        for i in range(26):
            if freq1[i] == freq2[i]:
                total_matches += 1

        # STEP 3: Slide the window across s2
        # j is the index of the new character entering the window
        for j in range(len(s1), len(s2)):
            
            # EARLY EXIT:
            # If all 26 characters match, we found a permutation
            if total_matches == 26:
                return True
            
            # -------------------------
            # HANDLE RIGHT (ENTERING) CHARACTER
            # -------------------------
            right_char = s2[j]
            idx = ord(right_char) - ord('a')

            # If this character was previously matching,
            # adding it will break the match
            if freq1[idx] == freq2[idx]:
                total_matches -= 1

            # Add the new character to the window
            freq2[idx] += 1

            # If after adding, the frequencies match again,
            # we restore the match count
            if freq1[idx] == freq2[idx]:
                total_matches += 1

            # -------------------------
            # HANDLE LEFT (EXITING) CHARACTER
            # -------------------------
            left_char = s2[left]
            idx = ord(left_char) - ord('a')

            # If this character was matching,
            # removing it will break the match
            if freq1[idx] == freq2[idx]:
                total_matches -= 1

            # Remove the character from the window
            freq2[idx] -= 1

            # If after removing, the frequencies match again,
            # we restore the match count
            if freq1[idx] == freq2[idx]:
                total_matches += 1

            # Move the window forward
            left += 1

        # Final check after the loop ends
        return total_matches == 26
    



# Revision Tip (Quick Recall)
    # 26 matches = perfect frequency match
    # Each slide:
    # Update right char (add)
    # Update left char (remove)
    # Adjust total_matches before and after frequency change

# ⏱️ Time Complexity
    # O(n)
    # Where n = len(s2)
    # Explanation:
    # Building initial frequency arrays takes O(|s1|)
    # Initial match count loop runs over 26 characters → O(26) ≈ O(1)
    # Sliding window iterates once over s2 → O(n)
    # Each window update does constant work (array access, comparisons)
    # ✅ Overall: O(n)

# 💾 Space Complexity
    # O(1) (constant space)
    # Explanation:
    # Two frequency arrays of fixed size 26
    # A few integer variables (left, total_matches, etc.)
    # No extra space grows with input size
    # ✅ Overall: O(1)






