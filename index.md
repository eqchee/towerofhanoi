# Cyclic Tower of Hanoi



## About The Project

In this variant of cyclic Tower of Hanoi, there are n disks distributed over 3 pegs, with disk size decreasing from bottom to top. This algorithm has been designed to compute the least moves needed so that all the disks are stacked on a single peg based on the following observations. 

- For the least number of moves:
  - The largest disk should not be moved. This means that all disks will eventually be stacked on the peg containing the largest disk, which will be known as the final peg.  
  - The 2nd largest disk would need to move in a direction which results in the least number of moves to move to the final peg. 
- Alternate size disks must move in opposite directions. If the 2nd largest disk needs to be moved in the clockwise direction, so must the 4th, 6th, etc largest disk, while the 3rd, 5th, etc largest disk would move in the counterclockwise direction 
- Sum up the number of moves required for each disk, starting from the 2nd largest disk to the smallest disk. 

- If the total number of moves needed is odd, the first disk to move must be the smallest disk. 



## Time Complexity

At worst case, the recursive function totalmoves() would have n-1 operations where n represents the number of disks and 
for each operation, it calls the function move() where there would be n operations to locate the disks. Thus, the total number of operations for totalmoves() would be n(n-1) = n^2 - n. As such, the time complexity of the algorithm would be O(n^2).

