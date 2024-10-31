

class Solution(object):
    def isPalindrome(self,x):
        solution = Solution()
        rev = solution.reverse_integer(x)
        print(f"Comparison of ", rev , " vs " , x)
        if rev == x:
            print(f"X IS a palindrome")
            return True
        else:
            print(f"X is NOT a palindrome")
            return False

    def reverse_integer(self,n):
        rev = 0
        while n > 0:
            digit = n % 10
            print(f"digit = {digit}")
            rev = rev * 10 + digit
            print(f"rev = {rev}" )
            n //= 10
        print(f"Reverse =", rev)
        return rev
if __name__ == "__main__":
    Solution().isPalindrome(123454321)

