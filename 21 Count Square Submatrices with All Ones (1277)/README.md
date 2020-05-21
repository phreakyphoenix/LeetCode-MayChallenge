# [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
[Challenge card](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/)
[Code Explanation Link](https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space))
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =\
[\
  [0,1,1,1],\
  [1,1,1,1],\
  [0,1,1,1]\
]\
Output: 15\
Explanation:\
There are 10 squares of side 1.\
There are 4 squares of side 2.\
There is  1 square of side 3.\
Total number of squares = 10 + 4 + 1 = 15. 

Example 2:

Input: matrix = 
[\
  [1,0,1],\
  [1,1,0],\
  [1,1,0]\
]\
Output: 7\
Explanation:\
There are 6 squares of side 1.\
There is 1 square of side 2.\
Total number of squares = 6 + 1 = 7.
 
Constraints:

1 <= arr.length <= 300\
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

Soln Explanation:
![img1](https://github.com/phreakyphoenix/LeetCode-MayChallenge/blob/master/21%20Count%20Square%20Submatrices%20with%20All%20Ones%20(1277)/assets/explanation1.png)
![img2](https://github.com/phreakyphoenix/LeetCode-MayChallenge/blob/master/21%20Count%20Square%20Submatrices%20with%20All%20Ones%20(1277)/assets/explanation2.png)
![img3](https://github.com/phreakyphoenix/LeetCode-MayChallenge/blob/master/21%20Count%20Square%20Submatrices%20with%20All%20Ones%20(1277)/assets/explanation3.png)
