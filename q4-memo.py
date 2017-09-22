# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:28:30 2017

@author: danna
"""

# Q3 (4)
#   1-2  2-3  - 1-3  [1,2,3]
#   2-1  1-3  - 2-3  [1,2,3]   2-1 wrong

#   1-2 1-3 2-1 2-3 
#   [3-4] [4-1] 3-1 wrong

#   if new element is not in the array, make possible arrays
#  [case 1] - correct
#   3-4  4-1  - 3-1  [4,1,2,3] 3-4 wrong, 3-1 wrong
#   4-3  3-2  - 4-2  [4,1,2,3] 3-2 wrong

#  [case 2]
#   3-4  4-1  - 3-1  [1,2,3,4] 4-1 wrong, 3-1 wrong
#   4-3  3-2  - 4-2  [1,2,3,4] 4-3 wrong, 3-2 wrong, 4-2 wrong


# Q4 correct (6)
# 1-2 2-4 4-3         [1, 2, 4, 3]
# 2-1 1-3     - 2-3   [1, 2, 4, 3] 2-1 wrong
# 3-4 4-1     - 3-1   [1, 2, 4, 3] 3-4 wrong, 4-1 wrong, 3-1 wrong
# 4-3 3-2     - 4-2   [1, 2, 4, 3] 3-2 wrong, 4-2 wrong

# Q5 correct (9)
# 1-2 2-3 3-4                  [1,2,3,4]
# 2-3 3-4 4-1  - 2-1  2-4      [1,2,3,4]  4-1 wrong, 2-1 wrong
# 3-4 4-1 1-2  - 3-2  3-1      [1,2,3,4]  4-1 wrong, 3-2 wrong, 3-1 wrong 
# 4-3 3-2 2-1  - 4-2  3-1      [1,2,3,4]  4-3 wrong, 3-2 wrong, 2-1 wrong, 4-2 wrong, 3-1 wrong

order(1, 1, 2).
order(1, 2, 3).
order(1, 3, 4).

1-2    0
2-3    1
3-4    2

1-3    00, 1 1
1-4    00, 1+1 1
       0+1 0, 1+1 1
#2-4

1,2,3,4,5

1-2
2-3
3-4
4-5
----------- for [0]
                for [1]
1-2
1-3
1-4
1-5

2-3
2-4
2-5

3-5




# Q6 correct (5)
# 1-2 2-3 +1-3  [1,2,3] 
# new element [4,1,2,3]   [1,4,2,3]   [1,2,4,3]
#
# [4,1,2,3]  -- correct
# 4-3, 3-2, +4-2      [4,1,2,3] 3-2 wrong
# 2-4, 4-1, +2-1      [4,1,2,3] 2-4 wrong, 2-1 wrong
# 1-3, 3-4, +1-4      [4,1,2,3] 3-4 wrong, 1-4 wrong
#
# [1,4,2,3]  -- correct
# 4-3, 3-2, +4-2      [1,4,2,3] 3-2 wrong
# 2-4, 4-1, +2-1      [1,4,2,3] 2-4 wrong, 2-1 wrong, 4-1 wrong
# 1-3, 3-4, +1-4      [1,4,2,3] 3-4 wrong
#
# [1,2,4,3]  -- correct
# 4-3, 3-2, +4-2      [1,2,4,3] 3-2 wrong, 4-2 wrong
# 2-4, 4-1, +2-1      [1,2,4,3] 2-1 wrong, 4-1 wrong
# 1-3, 3-4, +1-4      [1,2,4,3] 3-4 wrong