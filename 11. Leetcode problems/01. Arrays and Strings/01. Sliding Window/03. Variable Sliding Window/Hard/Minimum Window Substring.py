# Minimum Window Substring

# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if s is shorter than t, no valid window exists
        if len(s) < len(t):
            return ""

        # Step 1: Build a frequency map of characters required from t
        req_freq = {}
        for ch in t:
            req_freq[ch] = req_freq.get(ch, 0) + 1

        # Step 2: Initialize sliding window variables
        window_freq = {}           # Tracks frequencies of characters in current window
        left = 0                   # Left pointer of window
        best_left = 0              # Start index of minimum window found so far
        min_len = float("inf")     # Length of minimum window
        formed_matches = 0         # Number of characters meeting required frequency
        required_matches = len(req_freq)  # Number of unique characters to satisfy

        # Step 3: Expand the window by moving the right pointer
        for right in range(len(s)):
            rch = s[right]
            window_freq[rch] = window_freq.get(rch, 0) + 1

            # If the current character's count matches the required count, increment formed_matches
            if rch in req_freq and window_freq[rch] == req_freq[rch]:
                formed_matches += 1

            # Step 4: Shrink the window from the left as long as it remains valid
            while formed_matches == required_matches:
                current_len = right - left + 1
                if current_len < min_len:
                    # Update minimum window info
                    min_len = current_len
                    best_left = left

                # Remove the leftmost character from the window
                lch = s[left]
                window_freq[lch] -= 1

                # If removing this character causes it to drop below required frequency,
                # decrement formed_matches (window no longer fully valid)
                if lch in req_freq and window_freq[lch] < req_freq[lch]:
                    formed_matches -= 1

                # Move the left pointer forward to shrink window
                left += 1

        # Step 5: Return result
        # If no valid window found, return empty string
        return "" if min_len == float("inf") else s[best_left : best_left + min_len]




# | Aspect               | Complexity                                                      |
# | -------------------- | --------------------------------------------------------------- |
# | **Time Complexity**  | **( O(n + m) )**                                                |
# | **Space Complexity** | **( O(1) )** (fixed alphabet) / **( O(n + m) )** (general case) |
# | **Algorithm Type**   | Sliding Window + Hash Maps                                      |



# Building the frequency map for t: O(n)
# Sliding window over s: O(n)
# Inner while loop (shrinking window): Across the entire algorithm, left moves at most n times: O(n)
# O(m) + O(n) + O(n) = O(m + n)