# CMPS 2200 Recitation 06
## Answers

**Name:** Ella Moses



Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

Recurrence of work:

W(n) = W(n-1) + W(n-2) + 1

W(n) = O(2^n)

- **3)**

Recurrence of span:

S(n) = S(n-1) + S(n-2) + 1

S(n) = O(2^n)

- **4)**

For a value n, counts has n+1 terms. counts[1:] is equal to the reverse fibonacci sequence for n and counts[0] is equal to the n-1 element of the fibonacci sequence.

- **6)**

The maximum number of times that fib_top_down(i)will be called for any value i is 2. 

W(n) = O(n)
S(n) = O(n)


- **8)**

Maximum number of times that Fi will be read is 2 because it will be read when n = i + 1 and n  i - 1. 

W(n) = O(n)
S(n) = O(n)