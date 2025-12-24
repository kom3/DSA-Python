# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

# Topics
#     String
#     Sliding Window
#     Weekly Contest 190



# Pattern: Fixed Sliding Window + Running Count / Sum


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'} #using set over array for faster member checkup
        max_vowels_count = 0
        vowel_count_in_curr_window = 0

        # slide the window
        for i in range(len(s)): # observe the upperbound (i will become a right pointer), memorize this
            # add element right
            # initially, till the firt window of size k is formed, check each character entering the window and update the counter accordingly.
            if s[i] in vowels:
                vowel_count_in_curr_window += 1
            
            if i >= k - 1:
                # update/process
                max_vowels_count = max(max_vowels_count, vowel_count_in_curr_window)

                # remove left item
                # if the left item is vowel, then remving it will reduce the vowel_count_in_curr_window by 1 else no changes to that count

                # check if the left most item is an ovel
                if s[i - (k-1)] in vowels:
                    vowel_count_in_curr_window -= 1

        # return the final max count
        return max_vowels_count




# Total time complexity: O(n)

# Hints:
# max count of vowels in a given window size ever possible is  = k(window size) --> This can help with an early exit.
# Each time window slides, one character is leaving the window on left side and the new character is entering the window on right side --> this can help to reduce the recomputation of vowels count in the current window


        