# 1052. Grumpy Bookstore Owner

# There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1

# Output: 1

 

# Constraints:

# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104
# 0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.







from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # --------------------------------------------------
        # total_happy_cust:
        # Customers that are ALWAYS satisfied
        # (owner is NOT grumpy at that minute)
        # --------------------------------------------------
        total_happy_cust = 0

        # --------------------------------------------------
        # total_unhappy_cust:
        # Customers that are currently UNSATISFIED
        # inside the sliding window of size = minutes
        # (these can potentially be converted to happy)
        # --------------------------------------------------
        total_unhappy_cust = 0

        # --------------------------------------------------
        # max_unhappy_cust:
        # Maximum number of unhappy customers we can
        # convert to happy by applying the technique
        # in any window of length = minutes
        # --------------------------------------------------
        max_unhappy_cust = 0

        # --------------------------------------------------
        # SLIDING WINDOW over the timeline
        # --------------------------------------------------
        for i in range(len(customers)):

            # --------------------------------------------------
            # ADD RIGHT:
            # If owner is not grumpy, customers are always happy
            # If owner is grumpy, customers are unhappy and
            # can be potentially recovered by the technique
            # --------------------------------------------------
            if grumpy[i] == 0:
                total_happy_cust += customers[i]
            else:
                total_unhappy_cust += customers[i]

            # --------------------------------------------------
            # Once the window reaches size = minutes
            # --------------------------------------------------
            if i >= minutes - 1:

                # Update maximum recoverable unhappy customers
                max_unhappy_cust = max(max_unhappy_cust, total_unhappy_cust)

                # --------------------------------------------------
                # REMOVE LEFT:
                # Shrink the window by removing the element
                # that is sliding out of the window
                # --------------------------------------------------
                left = i - (minutes - 1)
                if grumpy[left] == 1:
                    total_unhappy_cust -= customers[left]

        # --------------------------------------------------
        # Final answer:
        # Always-happy customers +
        # Maximum unhappy customers converted to happy
        # --------------------------------------------------
        return total_happy_cust + max_unhappy_cust






# 🧠 Key Revision Takeaways:
# 1️⃣ Problem Insight
    # Customers during non-grumpy minutes are always satisfied
    # Customers during grumpy minutes are unhappy
    # You can convert unhappy → happy for one continuous window of minutes

# 2️⃣ Sliding Window Meaning
    # Window tracks unhappy customers that can be recovered
    # Goal: find window with maximum sum

# 3️⃣ Why only grumpy == 1 matters in the window
    # grumpy == 0 customers are already counted
    # Only unhappy customers benefit from the technique

# ⏱️ Time & Space Complexity
# Time	O(n)
# Space	O(1)