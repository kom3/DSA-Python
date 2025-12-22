🔹 Sliding Window Technique (From Zero → FAANG)

1️⃣ Why Sliding Window Exists (Very Important)

The problem it solves

Many problems ask:

    “Find something contiguous in an array or string”

Examples:

- ##### Maximum sum subarray of size k

- ##### Longest substring without repeating characters

- ##### Smallest subarray with sum ≥ X

Naive (Brute Force) Thinking

For every possible subarray:

Calculate its sum / count / condition

Time complexity: O(n²) ❌ (too slow for FAANG)

👉 Sliding Window reduces this to O(n)

2️⃣ What Is a Sliding Window?

Imagine a window (range) that moves over the array:

[ 2  1  5  1  3  2 ]
  ↑     ↑
 left  right


Instead of recomputing everything:

Add the new element entering the window

Remove the element leaving the window

This saves time.

3️⃣ Two Types of Sliding Window (MUST KNOW)
🔹 Type 1: Fixed Size Window

Window size is constant (k)

Examples:

Maximum sum of subarray of size k

Average of subarrays of size k

🔹 Type 2: Variable Size Window

Window expands and shrinks based on conditions

Examples:

- ##### Longest substring without repeating characters

- ##### Smallest subarray with sum ≥ target

4️⃣ Fixed Size Sliding Window (FOUNDATION)
Example Problem

- ##### Maximum sum of subarray of size k

        Input:
        nums = [2, 1, 5, 1, 3, 2]
        k = 3

        Brute Force ❌

        Check all subarrays of size 3 → O(nk)

        Optimal Sliding Window ✅
        Intuition

#### Calculate sum of first k elements

Slide window:

- Add next element

- Remove previous element

✅ Code (Python)

    def max_sum_subarray(nums, k):
        window_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            window_sum += nums[i]     # add element

            if i >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[i - (k - 1)]  # remove element

    return max_sum

⏱ Time & Space

    Time: O(n)

    Space: O(1)

5️⃣ Variable Size Sliding Window (FAANG FAVORITE)
Example Problem

- Longest Substring Without Repeating Characters

        Input: "abcabcbb"
        Output: 3  ("abc")

#### Key Idea

    Expand right pointer

    If condition breaks → shrink from left

🧠 Window Rules
| Step    | Action         |
|---------|----------------|
| Expand  | Move right     |
| Invalid | Shrink left   |
| Valid   | Update answer  |


✅ Code (Python)
def longest_unique_substring(s):
    
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

🔥 Interview Insight

    right - left + 1 → current window size

Shrinking ensures condition is valid

6️⃣ Universal Sliding Window Template (MEMORIZE)

    left = 0
    for right in range(n):
        # expand window
        add(nums[right])

        while window_invalid:
            remove(nums[left])
            left += 1

        update_answer()


🔥 90% of sliding window problems follow this

7️⃣ FAANG Sliding Window Patterns
Common Questions
- Pattern	Example
- Max/Min Subarray	Max sum of size k
- Longest Window	Longest substring
- Smallest Window	Min window substring
- Count Windows	Number of subarrays
8️⃣ Interview Red Flags 🚩

❌ Nested loops for subarrays
❌ Recomputing sum every time
❌ Forgetting to shrink window

9️⃣ Practice Problems (In Order)
### Beginner

Maximum sum subarray of size k

Average of subarrays of size k

### Intermediate

Longest substring without repeating characters

Longest subarray with sum ≤ k

### Advanced (FAANG)

Minimum Window Substring

Subarrays with exactly K distinct integers