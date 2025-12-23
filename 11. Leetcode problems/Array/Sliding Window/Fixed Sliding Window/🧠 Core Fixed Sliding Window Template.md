```
window_sum = 0
left = 0

for right in range(len(nums)):
    window_sum += nums[right]

    if right - left + 1 == k:
        # process window
        window_sum -= nums[left]
        left += 1

```

##### Memorize these points:


- __“Add right, process window, remove left”__

- __If Window Accumulator needed(like sum, diff, avg, compare threshold...etc):__ Upperbound of a "for" loop becomes length of array/string(that means index "i" starts from 0 and stopes at len(arr or str) - 1), ie **0 <= i < len(arr or str)**, where "k" is the window size.

- __If no Window Accumulator needed:__ Upperbound of a "for" loop becomes (length of array or string) - (k - 1), ie, **0 <= i < len(arr or str) - (k - 1)**, where "k" is the window size.

