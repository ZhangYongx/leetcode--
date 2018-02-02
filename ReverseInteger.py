"""
Given a 32-bit signed integer, reverse digits of an integer.
主要考虑 溢出
"""

# 本人答案
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            last=int(str(x)[::-1])
        else:
            x=-x
            last= -1 * int(str(x)[::-1])
        return last if last.bit_length() < 32 else 0
     
     
#leetcode 高票答案
def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)
