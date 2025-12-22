# Problem: Maximum sum of subarray of size k

# ---------------------------------------------------------------------------------


# 1. Brute Force Approach(Understand with an example dry run)

nums = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = 0
for i in range(len(nums) - (k-1)): #Prevent pointer going till last element, because sub-array needs atleast lenght k
    current_sum = 0
    sub_array = []
    for j in range(i, i + k): # from current index i to next two elements(total three elements required in a sub array)
        # find sum of current sub array elements
        sub_array.append(nums[j])
        current_sum += nums[j]
    print(f"sub array {i+1}: { sub_array }")
    max_sum = max(max_sum, current_sum)

print(f"Max sum of a sub-array of size {k} is {max_sum}")

# Time complexity: O(n * k), This only becomes O(n²) if k ≈ n, but in general interviews expect O(nk).
# This solution runs in O(nk) time, which is inefficient when k is large

# with sub_array(used for printing purpose) Space complexity: O(n) if k ≈ n, but in general interviews expect O(k).
# Space complexity becomes O(1) if there is no sub_array used.

# output: 
# sub array 1: [2, 1, 5]
# sub array 2: [1, 5, 1]
# sub array 3: [5, 1, 3]
# sub array 4: [1, 3, 2]
# Max sum of a sub-array of size 3 is 9





# 2. Optimal Sliding Window Approach

def max_sub_array(nums, k):
    max_sum = 0
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[i - (k - 1)] # or (i - k + 1)

    return max_sum

result = max_sub_array(nums, k)

print(f"Max sum of a sub-array of size {k} is {result}")

# Output:
# Max sum of a sub-array of size 3 is 9





