class Solution:
    # @params A: a file containing scores received by students in a number of subjects
    # returns: an integer: a number of students have aggregates scores of 100 or more.
    # output.txt file contains 2, if two students have aggregates scores of 100 or more.
    def numberOfHighScorer(self, A):
        data = {}
        with open(A, 'r') as file:
            for line in file:
                id, subject, marks = line.strip().split(',')

                data[id] = data.get(id, 0) + int(marks)

            # Prints number of students have aggregates scores of 100 or more.
            print(len([key for key, value in data.items() if value >= 100]))

# Use cases
if __name__ == '__main__':
    s = Solution()
    A = 'input.txt'
    s.numberOfHighScorer(A)
