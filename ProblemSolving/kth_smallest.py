# Find kth smallest element in an unsorted array
class Solution:
    ## @params A, k: a list, kth value
    ## @return: an integer
    def kthSmallest(self, A, n, k):

        # sort the list
        A.sort()
        # Return k'th element in the sorted array

        return A[k-1]

# Test code
if __name__=='__main__':
    s = Solution()
    A = [12, 3, 5, 7, 19]
    n = len(A)
    k = 2
    print('Kth smallest element is', s.kthSmallest(A, n, k))
