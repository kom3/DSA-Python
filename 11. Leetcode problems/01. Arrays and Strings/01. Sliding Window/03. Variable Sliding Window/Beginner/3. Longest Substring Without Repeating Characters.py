# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.






class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores the maximum length of a substring without repeating characters
        max_len = 0
        
        # Left pointer of the sliding window
        left = 0
        
        # Dictionary to store the last seen index of each character
        seen = {}

        # Right pointer moves through the string
        for right in range(len(s)):
            # If the current character was seen before AND
            # it lies within the current window
            if s[right] in seen and seen[s[right]] >= left:
                # Move the left pointer to one position after
                # the last occurrence of the current character
                left = seen[s[right]] + 1
            
            # Update the last seen index of the current character
            seen[s[right]] = right
            
            # Update the maximum window size found so far
            max_len = max(max_len, right - left + 1)

        # Return the length of the longest valid substring
        return max_len




# Solution 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            rch = s[right]

            while rch in seen:
                seen.remove(s[left])
                left += 1

            seen.add(rch)
            max_len = max(max_len, right - left + 1)

        return max_len
