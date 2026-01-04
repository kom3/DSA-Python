# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.





from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group anagrams
        # key   -> character frequency tuple
        # value -> list of strings with that frequency pattern
        groups = {}

        for word in strs:
            # Frequency array for 26 lowercase English letters
            freq = [0] * 26

            # Count each character in the word
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            # Convert list to tuple so it can be used as a dictionary key
            key = tuple(freq)

            # Append the word to its corresponding anagram group
            groups.setdefault(key, []).append(word)

        # Return all grouped anagrams
        return list(groups.values())


# Time and Space complexities:
# Time: O(n * k)
# Space: O(n * k)





from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store groups of anagrams
        # Key: sorted version of the string
        # Value: list of strings that are anagrams of each other
        anagram_groups = {}

        for s in strs:
            # Sort the string to create a key
            # All anagrams will have the same sorted string
            key = "".join(sorted(s))

            # Append the original string to its corresponding group
            # If the key doesn't exist, initialize with an empty list
            anagram_groups.setdefault(key, []).append(s)

        # Return all groups of anagrams as a list of lists
        return list(anagram_groups.values())



# Time Complexity
# Sorting each string of length k: O(k log k)
# Doing this for n strings: O(n * k log k)

# Space Complexity
# Dictionary stores all strings and keys: O(n * k)