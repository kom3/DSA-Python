## 🔑 Core Linked List Rules (Must Remember)

1. **Head is mandatory** in every linked list
   → Without head, you lose access to the list.

2. **Tail is optional** in all linked lists
   → Used only for optimization (faster insertion at end).

3. **No random access**
   → You must traverse from head (O(n)).

4. **Dynamic size**
   → No fixed size like arrays.

5. **Non-contiguous memory allocation**

---

## 🔹 Singly Linked List (SLL)

* Each node has:

  ```python
  data + next
  ```
* Traversal only in **one direction**
* Insert/delete at front → **O(1)**
* Insert/delete at end → **O(n)** (O(1) if tail exists)

**Interview tip:**

> “SLL is memory-efficient but traversal is one-way.”

---

## 🔹 Doubly Linked List (DLL)

* Each node has:

  ```python
  data + prev + next
  ```
* Traversal in **both directions**
* More memory than SLL
* Deletion is easier (no need to track previous node)

**Interview tip:**

> “DLL trades extra memory for easier operations.”

---

## 🔹 Circular Linked List

* Last node points back to **head**
* No `NULL` pointer
* Traversal can start from **any node**

### Circular Singly

* `tail.next = head`

### Circular Doubly

* `tail = head.prev`
* `tail.next = head`

**Interview tip:**

> “In circular lists, tail can be accessed via head.”

---

## ⏱ Time Complexity Cheatsheet

| Operation       | SLL          | DLL   |
| --------------- | ------------ | ----- |
| Insert at front | O(1)         | O(1)  |
| Insert at end   | O(n) / O(1)* | O(1)* |
| Delete front    | O(1)         | O(1)  |
| Delete end      | O(n)         | O(1)* |
| Search          | O(n)         | O(n)  |

* with tail pointer

---

## ⚠️ Common Interview Traps

1. **Forgetting edge cases**

   * Empty list
   * Single node
   * Deleting head or tail

2. **Breaking circular links**

   * Always update last node when head changes

3. **Losing head reference**

   * Never overwrite head without saving it

---

## 💡 One-Line Answers (Gold for Interviews)

* **Why linked list over array?**
  → Dynamic size and efficient insertions/deletions.

* **Why DLL over SLL?**
  → Bidirectional traversal and easier deletion.

* **Why tail pointer?**
  → To make insertion at end O(1).

* **Why circular list?**
  → Continuous traversal without NULL checks.

---

## 🧠 Memory Comparison

```text
SLL   → least memory
DLL   → more memory
CDLL  → most flexible
```

---

## 🎯 Final Tip

If you remember just **3 things**, remember these:

1. **Head is mandatory**
2. **Tail is optional**
3. **Traversal cost is O(n)**
