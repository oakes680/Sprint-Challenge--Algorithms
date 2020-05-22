# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

O(n)         Space O(1)


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(nlogn)         Space O(1)


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

      O(n)   space O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
Egg Drop average  O(n)


Binary Search.    cut the floors in half each time   O(logn)   

We will start on the ground floor.   Find the middle floor.
Then drop the egg  - >  there are two possibilities the egg breaks or the egg doesn't break.
1.) if the egg breaks -   We will move from the middle floor down to a new middle floor which is the middle between the ground and the current floor you are on.  
2.) If the egg doesn't break we will move to the middle floor between the current floor you are on and the top floor.
repeat until you find the highest floor the egg doesn't break on.

