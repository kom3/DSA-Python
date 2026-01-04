# 271. Encode and Decode Strings

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: dummy_input = ["Hello","World"]

# Output: ["Hello","World"]

# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:

# Input: dummy_input = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible set of characters?






from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Format: <length>#<string>
        Example: ["abc", "de"] -> "3#abc2#de"
        """
        encoded = []

        for s in strs:
            # Append the length of the string, a delimiter '#',
            # and the string itself
            encoded.append(f"{len(s)}#{s}")

        # Join all encoded parts into one string
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single encoded string back into a list of strings.
        """
        res = []          # Result list
        start = 0         # Pointer to track current position in string

        while start < len(s):
            count = 0

            # Read characters until '#' to get the string length
            while s[start] != "#":
                count = count * 10 + int(s[start])
                start += 1

            # Skip the '#' character
            start += 1

            # Extract the string of length `count`
            res.append(s[start:start + count])

            # Move pointer to the start of the next encoded string
            start += count

        return res
    





# Time Complexity: O(n)
# Space Complexity: O(n)

