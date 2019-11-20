# Simplify Directory Path
# https://www.interviewbit.com/problems/simplify-directory-path/
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# Examples:
#
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):

        head = last = None
        while A:
            start = A
            prev = A
            A = A.next
            for i in range(1, B):
                next = A.next
                A.next = prev
                prev = A
                A = next
            if last:
                last.next = prev
            last = start

            if not head:
                head = prev
        if last:
            last.next = None

        return head



