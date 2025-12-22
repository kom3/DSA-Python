left = 0
window = {}
result = 0

for right in range(len(nums)):

```
    # expand window
    window[nums[right]] = window.get(nums[right], 0) + 1

    # shrink window while condition not met
    while not is_valid(window):
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            del window[nums[left]]
        left += 1

    # update result
    result = max(result, right - left + 1)
```


Key pattern: Expand → Check → Shrink → Update result