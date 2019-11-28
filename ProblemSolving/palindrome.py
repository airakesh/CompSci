'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = ''.join(c.lower() for c in A if c.isalnum())
        # print(A)
        # print(A[::-1])
        if A == A[::-1]:
            return 1
        else:
            return 0

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(''))
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
    print(s.isPalindrome('race a car'))
