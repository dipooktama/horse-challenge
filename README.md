# horse-challenge

## brief
given there are 25 horses, find the 3 fastest horses with this rule:
1. only 5 horses can be competed at one time
2. you can't measure the time

## my solution
my solution is to mock a 25 horses with a random number from 1 to 99 as an 5x5 array
each number is their corresponding speed and then loop them over and compare them.

### 1st horse
- then I will sort each 'rows' in descending manner
- sort the array based on each first index
- the first index from the first array is the 1st horse

### 2nd horse
- competing the first index from second array against the 1st horse's array
- if it wins, then it it becomes the 2nd horse
- if not, then pick the first index from that race

### 3rd horse
- from the second race, if the first index from the second array lose against the 1st horse's array, then pick the second index as the 3rd horse. (this will result in only 2 race)
- if not, then compete the first index from the third array against the 1st horse's array
- pick the first index from that race. (this will result in 3 race)

## final thoughts
it's fun. I tried to do a complex array stuffs at the first place, but resort to a simple loop and if block at the end.

Also, I think this can be resolved with recursion.
