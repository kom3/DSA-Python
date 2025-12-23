# 1461. Check If a String Contains All Binary Codes of Size K

# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20






# Stright away we think that the problem is asking to compare all the binary codes(subsequences) of size k with the available sub strings of sizek
# But the fact is we can come to the conclusion of whether all the possible binary codes(subsequences) of size k present as substrings just by checking the count without doing the actual content comparision(comparing all combinations of binary codes with available substrings).
# We know there are two possible numbers in binary, so the max possible combinations can be calculated as 2^k and this should match the number of unique substrings of length k.


# We can generate substrings of given size  using sliding window.
# Because calculating the all possible binary codes of size k is not a sliding window problem, it's more of a combinatorics(permutaions & combinations) problem. so instead we just find how many possible combinations of given size can be formed using 2^k formula



# Solution 1
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # if window size is greater than length of strings, exit (edge case)
        if k > len(s):
            return False

        unique_substrings = set()
        curr_window_sub_str = ""

        for i in range(len(s)):
            # add a new element on right
            curr_window_sub_str += s[i]

            if i >= k - 1:
                # add new subarray to a set
                unique_substrings.add(curr_window_sub_str)
                # remove first char which is leaving the window on left
                curr_window_sub_str = curr_window_sub_str[1:]
            
        if pow(2, k) == len(unique_substrings):
            return True
            
        return False


s = "0110"; k = 2

sobj = Solution()

print(sobj.hasAllCodes(s, k))


# Performance
    # Time Complexity: O(n*k) because slicing strings takes O(k) each time.
    # Space Complexity: O(2^k * k) because you store each unique substring.
    # For large k (like 20), this could be slow sometimes, might crash as well if "k" is too large.
    # Above code has a string slicing operation which is going to be expensive, so let's try for alternate optimal solutions.






# Solution 2
    # Sliding Window Pattern Summary
    # Initialize: 
        # num = 0,  later it acts as a container to store the binary nums from of the given input string
        # mask = (1 << k) - 1, this is a formula to calculate the mask(memorize), it can also be written as (2^k -1), so 2^k is 1 << k
        # unique_set = set(), this to store the substrings of binary nums of given size "k"
    
    # Below is the sliding window logic for binary string
        # Loop through string s
        # Update num with num = ((num << 1) | int(s[i])) & mask
        # Add num to set once window size ≥ k
        # Check if len(unique_set) == 2**k → all codes exist

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        # initialize
        num = 0
        mask = (1 << k) - 1 # formula to calculate mask for given k (memorize)
        seen = set()

        # sliding window logic
        for i in range(len(s)):
            # update num
            num = ((num << 1) | int(s[i])) & mask # memorize this, this is a standard way of removing left bit and adding new bit on right

            # once window created, process
            if i >= k - 1:
                seen.add(num)

                # Early exit: if all codes are found (memorise, wihtout this check whole logic fails, so this check is a must)
                if pow(2, k) == len(seen):
                    return True
        
        # check if number of binary substrings in the set seen are equal to the total number of combinations for a given size k

        return pow(2, k) == len(seen)

        






# Solution3
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sl = len(s)
        need = 1 << k
        if sl - k + 1 < need:
            return False

        seen = [0] * need
        count = 0

        val = 0
        for i in range(k - 1):
            val <<= 1
            val += int(s[i])

        mask = need - 1
        for i in range(k - 1, sl):
            val = ((val << 1) & mask) | (ord(s[i]) & 1)
            if not seen[val]:
                seen[val] = 1
                count += 1
                if count == need:
                    return True

        return False

        
        




