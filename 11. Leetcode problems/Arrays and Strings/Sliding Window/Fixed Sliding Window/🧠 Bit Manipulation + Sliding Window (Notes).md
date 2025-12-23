Here are **clean, focused notes** you can keep and revise whenever you see **bit manipulation + sliding window** problems. Think of this as your **mental template**. 📘

---

# 🧠 Bit Manipulation + Sliding Window (Notes)

## 1️⃣ When to use this technique

Use **bit manipulation sliding window** when:

* The input is **binary** (`0` / `1`)
* You need to track **fixed-size substrings/windows**
* You want to avoid **string slicing**
* You need **fast performance** (`O(n)`)

Typical problems:

* Binary substrings of size `k`
* Checking uniqueness of binary patterns
* Rolling hash–like problems (but simpler)

---

## 2️⃣ Core idea (most important)

👉 **Represent a binary substring as an integer instead of a string**

Example:

```
"101" → 5
"011" → 3
```

This lets you:

* Slide the window using bit shifts
* Store results efficiently in a set

---

## 3️⃣ The sliding window formula (MEMORIZE THIS)

```python
num = ((num << 1) | new_bit) & mask
```

### What each part does:

| Part       | Meaning                 |                          |
| ---------- | ----------------------- | ------------------------ |
| `num << 1` | Shift window left       |                          |
| `          | new_bit`                | Add new bit on the right |
| `& mask`   | Keep only last `k` bits |                          |

---

## 4️⃣ Mask creation (VERY IMPORTANT)

```python
mask = (1 << k) - 1
```

### Why it works:

* `1 << k` → `1000...0` (k zeros)
* Subtract 1 → `0111...1` (k ones)
* AND with mask → keeps last `k` bits

Example (`k = 3`):

```
mask = 0111
num  = 1101
num & mask = 0101   ✅
```

---

## 5️⃣ Window size control

You only start using the window **after `k` elements**:

```python
if i >= k - 1:
    add num to set
```

This ensures:

* You only track valid windows
* No partial windows

---

## 6️⃣ Why this is efficient

| Approach         | Time   | Space |
| ---------------- | ------ | ----- |
| String slicing   | O(n·k) | High  |
| Bit manipulation | O(n)   | O(2ᵏ) |

✔ No slicing
✔ No extra strings
✔ Fast comparisons

---

## 7️⃣ Pattern to memorize (Template)

```python
num = 0
mask = (1 << k) - 1
seen = set()

for i in range(len(s)):
    num = ((num << 1) | int(s[i])) & mask
    if i >= k - 1:
        seen.add(num)
```

This template works for **many binary sliding window problems**.

---

## 8️⃣ Mental model (important!)

Think of bits as a **conveyor belt**:

```
[old bits] → shift left → add new bit → cut overflow
```

The **mask is scissors ✂️** that cuts off bits that fall out of the window.

---

## 9️⃣ Common mistakes to avoid

❌ Forgetting `& mask` → number grows too large
❌ Adding to set before window size = `k`
❌ Using strings when bits are enough

---

## 🔑 One-line memory hack

> **Shift → Add → Mask → Store**

If you remember this, you can solve most bit-sliding-window problems.

---

