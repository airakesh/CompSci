'''Find if there are two elements wtih given sum'''
# Time Complexity: O(n)
# Auxiliary Space: O(n) where n is size of array.

class Solution:
     def pairSum(self, A, k):
     
         s = set()
     
         for i in range(len(A)):
             temp = k - A[i]
     
             if temp in s:
                print((A[i], temp))
     
             s.add(A[i])

# Test cases
if __name__ == "__main__":
    s = Solution()
    A = [1, 12, 4, 45, 6, 10, -8]
    k = 16
    s.pairSum(A, k)
