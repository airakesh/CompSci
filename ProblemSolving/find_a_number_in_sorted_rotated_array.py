# Search an element in sorted and rotated Array
def search(A, low, high, B):
    if low > high:
        return -1

    mid = (low + high) // 2
    if A[mid] == B:
        return mid

    # If A[left...mid] is sorted
    if A[low] <= A[mid]:

        # As this subArray is sorted, we can quickly check if B lies in half or other half
        if B >= A[low] and B <= A[mid]:
            return search(A, low, mid - 1, B)
        return search(A, mid + 1, high, B)

    # If A[left..mid] is not sorted, then A[mid... right] must be sorted
    if B >= A[mid] and B <= A[high]:
        return search(A, mid + 1, high, B)
    return search(A, low, mid - 1, B)


if __name__ == '__main__':
    A = [4, 5, 6, 7, 0, 1, 2]
    B = 4 # target
    low = 0
    high = len(A) - 1
    print(search(A, low, high, B))


