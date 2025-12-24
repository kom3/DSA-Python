
## 🪟 Sliding Window Roadmap (Interview-Oriented)

Since you’re doing DSA seriously (4 hrs/day) and asking *why* patterns work, this roadmap is designed to help you **learn the sliding window pattern itself**, not just grind random problems.

The problems are grouped so your brain learns:

* *when* sliding window applies
* *why* it works
* *how* difficulty increases

---

## 🟢 Level 1: Fixed-Size Window (Foundations)

🔹 **What’s happening here?**
The window size `k` is fixed. You slide it forward by:

* removing the left element
* adding the right element

This is the **entry point** to sliding window.

**Core pattern to remember:**
➡️ *Remove left → Add right → Update answer*

### Problems to practice

* **643. Maximum Average Subarray I** (Easy)
  *Your very first fixed window problem.*

* **1343. Number of Sub-arrays of Size K and Avg ≥ Threshold** (Easy)
  *Fixed window + counting logic.*

* **2461. Maximum Sum of Distinct Subarrays With Length K** (Medium)
  *Introduces HashSet inside a window.*

* **1876. Substrings of Size Three with Distinct Characters** (Easy)
  *Sliding window over strings.*

* **2090. K Radius Subarray Averages** (Medium)
  *Helps compare prefix sums vs sliding window.*

* **1423. Maximum Points You Can Obtain from Cards** (Medium)
  *Classic trick: window from both ends.*

---

## 🟡 Level 2: Variable-Size Window (Most Important)

🔹 **What changes now?**
The window **expands and shrinks** depending on constraints.

This is the pattern that appears **most often in interviews**.

**Core pattern to remember:**
➡️ *Expand → Condition breaks → Shrink until valid*

### Problems to practice

* **3. Longest Substring Without Repeating Characters** (Medium)
  *The most asked sliding window question.*

* **424. Longest Repeating Character Replacement** (Medium)
  *Frequency map + window resizing.*

* **1004. Max Consecutive Ones III** (Medium)
  *Binary window with limited flips.*

* **209. Minimum Size Subarray Sum** (Medium)
  *Minimum window template.*

* **904. Fruit Into Baskets** (Medium)
  *“At most K distinct” pattern.*

* **713. Subarray Product Less Than K** (Medium)
  *Multiplicative sliding window.*

* **1248. Count Number of Nice Subarrays** (Medium)
  *Odd/even logic inside a window.*

* **2024. Maximize the Confusion of an Exam** (Medium)
  *Binary constraints + window.*

---

## 🔵 Level 3: Frequency + Map-Based Windows

🔹 **What’s the focus here?**
Character counts.
Anagrams.
Required vs formed characters.

These problems **show up everywhere**.

**Core pattern to remember:**
➡️ *Track required counts vs current window counts*

### Problems to practice

* **567. Permutation in String** (Medium)
  *Classic anagram detection.*

* **438. Find All Anagrams in a String** (Medium)
  *Same idea, multiple answers.*

* **76. Minimum Window Substring** (Hard)
  *The most famous hard sliding window problem.*

* **340. Longest Substring with At Most K Distinct Characters** (Medium)
  *Core frequency map logic.*

* **395. Longest Substring with At Least K Repeating Characters** (Medium)
  *Window combined with divide-and-conquer thinking.*

⚠️ **Important:** Don’t attempt problem 76 too early — it hides the basics and confuses beginners.

---

## 🔴 Level 4: Advanced / Tricky Sliding Windows

🔹 **What makes these hard?**
Sliding window combined with:

* deques
* prefix sums
* sorting
* tricky counting rules

**Core pattern to remember:**
➡️ *Sliding window + extra data structure*

### Problems to practice

* **239. Sliding Window Maximum** (Hard)
  *Deque + window.*

* **862. Shortest Subarray with Sum at Least K** (Hard)
  *Prefix sum + deque.*

* **1695. Maximum Erasure Value** (Medium)
  *Unique elements + window sum.*

* **992. Subarrays with K Different Integers** (Hard)
  *Exactly-K trick.*

* **930. Binary Subarrays With Sum** (Medium)
  *Binary window + prefix ideas.*

* **1838. Frequency of the Most Frequent Element** (Medium)
  *Sorting + sliding window.*

---

## 🧠 How to Study This (Interview-Focused Plan)

A realistic plan:

* **Day 1:** Fixed windows (Level 1)
* **Days 2–5:** Variable windows (Level 2)
* **Days 6–7:** Frequency windows (Level 3)
* **After that:** Advanced problems as stretch goals

---

## 🔑 Interview Insight (Very Important)

Not every “size k” problem uses sliding window.

Ask yourself:

* Is it a **contiguous** subarray or substring? → Sliding window ✅
* Can I pick elements in any order? → Sorting / combinations ❌

---

