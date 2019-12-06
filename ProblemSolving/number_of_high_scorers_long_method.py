'''
In this problem, you have to write a program that reads a file containing scores
received by students in a number of subjects, and does some processing on it.
The input is being read in from a file called input.txt, in this format:

22, Data Structures, 45
23, English, 52
22, English, 51
26, Data Structures, 72
23, Data Structures, 61
26, English, 81
27, English, 50
29, Operating System, 20
28, Database, 20
30, Operating System, 76
24, Programming Language, 96

Each line consists of three fields "Student ID," "Subject," and "Marks." "Student ID" and "Marks"
are integers and "Subject" is a string that does not contain commas or newlines. There can be any
number of students and up to 6 subjects.

Your program should read this file, count the number of students
whose total marks across all subjects is 100 or more, and write the count to a file called output.txt.

For example, if your program is run with the input given above, then at the end the file output.txt
should contain just 2.

That's because 2 students (with ID 23 and 26) have aggregates scores of 100 or more.
'''
class Solution:
    # @params A: a file containing scores received by students in a number of subjects
    # returns: a list of student IDs who scored >= 100

    def numsHighScorers(self, A):
        # Check if the file doesn't exist
        if not A:
            return -1
       # list of each column
        with open(A, 'r') as file:
            itemList = file.read().splitlines()
            # list of student IDs
            student_id = []
            # list of Subjects
            subject = []
            # list of students marks
            smarks = []

            # split each row in columns
            for item in itemList:
                if item != '':
                    first, second, third = item.split(',')
                    student_id.append(first.strip())
                    subject.append(second.strip())
                    smarks.append(third.strip())

            # Unique student IDs list
            student_idList = list(set(student_id))

            # Dictionary of students and their marks
            d = {}

            for i in range(len(student_id)):

                for row in range(len(student_idList)):

                    if student_idList[row] == student_id[i]:

                        # If students ID doesn't exist, add the keys (student IDs) and
                        # their values (marks) to corresponding student IDs
                        if student_idList[row] not in d:
                            marks = int(smarks[(i)])
                            d[student_idList[row]] = marks

                        # If a student ID exists, add the current value (marks)
                        # to the existing value (marks) corresponding that student ID (key)
                        else:
                            marks = int(smarks[(i)])
                            d[student_idList[row]] = d.get(student_idList[row], 0) + marks

            # Created a dictionary with Student IDs as keys and their total marks they scored as values.
            # return d

            # Prints student IDs and their total marks who scored => 100.
            for key, value in d.items():
                if value >= 100:
                    yield key


# Use cases
if __name__ == '__main__':
    s = Solution()

    # Input file
    A = 'input.txt'
    highScorer = s.numsHighScorers(A)
        
    # Writing output into output.txt
    with open('output.txt', 'w+') as fw:
        for student in highScorer:
            if student is not None:
                fw.writelines(student + '\n')
            else:
                print('No File Exists!')
                
 # output.txt 
23
26
