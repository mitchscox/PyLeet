# Author: (+)
# Notes: two sum leet code problem
#print("Leet Code problem here: https://leetcode.com/problems/two-sum/")
import argparse


#nums = [2,7,11,15]
#target = 9
#print("Nums list =" , nums)
#print("Target =", target)


class Solution(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='LeetCode problem on which needs a list of nums and a target.')
        self.parser.add_argument('target', type=float, help='The target number.')
        self.parser.add_argument('nums', type=list, help='List of integers.')

    def parse_args(self):
        args = self.parser.parse_args()
        return args

     

    def two_sum(nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            print("i = ", i)
            print("num =", num)
            complement = target - num
            print("complement = ", complement)
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

#solution = Solution()
#print("Indexes =", Solution.two_sum(nums, target))

if __name__ == "__main__":
    Solution.two_sum(nums, target)
