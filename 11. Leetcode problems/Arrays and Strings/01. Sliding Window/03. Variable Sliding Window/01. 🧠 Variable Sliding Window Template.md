##### Master template

```
left = 0
state = {}        # or set / count / sum / freq map
answer = 0        # max, min, or count

for right in range(len(arr)):
    # 1️⃣ Expand window
    add arr[right] to state

    # 2️⃣ Shrink window until valid
    while window is invalid:
        remove arr[left] from state
        left += 1

    # 3️⃣ Update answer (window is valid here)
    update answer using (right - left + 1)

return answer

```


##### Python code version

```
left = 0
window = {}
result = 0

for right in range(len(nums)):

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


__Key pattern: Expand → Check → Shrink → Update result__