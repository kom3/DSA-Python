window_sum = 0
left = 0

```
for right in range(len(nums)):
    window_sum += nums[right]

    if right - left + 1 == k:
        # process window
        window_sum -= nums[left]
        left += 1

```

“Add right, process window, remove left”