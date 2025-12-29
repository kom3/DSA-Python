# 904. Fruit Into Baskets

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to store count of each fruit type in the current window
        seen = {}

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum number of fruits collected
        max_len = 0

        # Right pointer expands the window
        for right in range(len(fruits)):

            # Add current fruit to the window
            seen[fruits[right]] = seen.get(fruits[right], 0) + 1

            # If more than 2 fruit types are present, shrink the window
            while len(seen) > 2:
                # Remove fruit at the left pointer
                seen[fruits[left]] -= 1

                # If count becomes zero, remove it from the dictionary
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]

                # Move left pointer to shrink the window
                left += 1

            # Update maximum window size (valid window with ≤ 2 fruit types)
            max_len = max(max_len, right - left + 1)

        # Return the maximum number of fruits collected
        return max_len





# ⏱️ Time Complexity
    #     O(n)
    #     Each fruit is added to the window once (right pointer)
    #     Each fruit is removed from the window once (left pointer)
    #     No nested reprocessing → linear scan

# 🧠 Space Complexity
    #     O(1)
    #     The dictionary seen stores at most 2 fruit types
    #     Space does not grow with input size