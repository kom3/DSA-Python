# 1876. Substrings of Size Three with Distinct Characters

# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
 

# Constraints:

# 1 <= s.length <= 100
# s​​​​​​ consists of lowercase English letters.


# Pattern: Fixed sliding window + boolean / set for uniqueness check

# Solution 1
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        good_str_count = 0

        for i in range(len(s) - (k - 1)):
            if len(set(s[i : i + k])) == len(s[i : i + k]):
                good_str_count += 1

        return good_str_count
    

# Time Complexity:
    # General case: O(n · k) , for loop + slice operation
    # For this problem (k = 3): O(n)

# Space Complexity:
    # O(1):  as k is a constant




# Solution 2 (more optimized for a variable "k" size and to reduce the uniqueness checking cost)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        good_str_count = 0

        for i in range(len(s)):
            if i >= k-1:
                # a != b and b != c and c != a (important condition for this problem)
                if s[i - (k - 1)] != s[i - (k - 2)] and s[i - (k - 2)] != s[i] and s[i] != s[i - (k - 1)]:
                    good_str_count += 1

        return good_str_count


so = Solution()
s = "xyzzaz"
print(so.countGoodSubstrings(s))



# Time Complexity
    # Single loop over the string → O(n)
    # Constant-time comparisons inside the loop
    # 👉 Overall: O(n)

# 🧠 Space Complexity
    # Only integer counters
    # No sets, no extra data structures, so faster than set() 
    # 👉 O(1) space due to zero allocations

