'''Find if there are two elements wtih given sum'''
# o(nlogn) and o(1) space

        def pairSum(self, A, k):

            A.sort()

            left = 0
            right = len(A) - 1

            while left < right:
                current_sum = A[left] + A[right]

                if current_sum == k:
                    print(A[left], A[right])
                    left += 1
                    right -= 1

                if current_sum > k:
                    right -= 1

                if current_sum < k:
                    left += 1
                #
                # list1 = [1, 8, 3, 2, 7]
                # pairSum(list1, 10)

# Test cases
if __name__ == "__main__":
    s = Solution()
    A = [1, 12, 4, 45, 6, 10, -8]
    k = 16
    s.pairSum(A, k)
