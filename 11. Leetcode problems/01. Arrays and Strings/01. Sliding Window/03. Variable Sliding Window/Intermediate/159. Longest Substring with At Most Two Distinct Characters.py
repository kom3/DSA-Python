# 159. Problem: Longest Substring with At Most Two Distinct Characters

# Given: A string s.

# Task: Find the length of the longest substring that contains at most two distinct characters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Dictionary to store frequency of characters in current window
        window = {}
        
        # Maximum length of substring found so far
        max_len = 0
        
        # Left pointer of the sliding window
        left = 0
        
        # Iterate over the string with right pointer
        for right in range(len(s)):
            # -------- Expand window --------
            # Add current character to the window
            window[s[right]] = window.get(s[right], 0) + 1
            
            # -------- Shrink window if invalid --------
            # Window is invalid if it has more than 2 distinct characters
            while len(window) > 2:
                # Remove the character at the left pointer
                window[s[left]] -= 1
                
                # If count becomes zero, remove it from the dictionary
                if window[s[left]] == 0:
                    del window[s[left]]
                
                # Move left pointer to shrink the window
                left += 1
                
            # -------- Update maximum length --------
            # Only valid windows (≤ 2 distinct characters) are considered
            max_len = max(max_len, right - left + 1)
            
        return max_len
    





    

# -------- Test Harness --------
ss = Solution()

testcases = [
    "eceba",               # Expected: 3
    "ccaabbb",             # Expected: 5
    "aaaaaa",              # Expected: 6
    "ababab",              # Expected: 6
    "abcabcbb",            # Expected: 4
    "a",                   # Expected: 1
    "",                    # Expected: 0
    "abaccc",              # Expected: 4
    "abcbbbbcccbdddadacb" # Expected: 10
]

expected_results = [3, 5, 6, 6, 4, 1, 0, 4, 10]

for idx, item in enumerate(testcases):
    try:
        res = ss.lengthOfLongestSubstringTwoDistinct(item)
        assert res == expected_results[idx]
        print(f"PASS: {item} → {expected_results[idx]}")
    except:
        print(f"FAIL: Input: {item}, expected: {expected_results[idx]}, got: {res}")




                

# Time: O(n) — each character is processed at most twice (once when added, once when removed).

# Space: O(1) — the window dictionary stores at most 2 keys.