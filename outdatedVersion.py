Find out of Oudated Servers from the list of the servers.

Input file (serverlist.txt) containing:
Server1, Database, MySQL, 5.5
Server2, Database, MySQL, 5.1
Server3, OS, Ubuntu, 10.04
Server1, OS, Ubuntu, 12.04
Server2, OS, Ubuntu, 12.04
Server3, Language, Python, 2.6.3

Output:
Server2
Server3
'''

class Solution:
    # @params A: a file containing list of software with their lower and upper version
    # returns: a list of versions name which are outdated
    def serverOutdated(self, A):
        # Check if the file doesn't exist
        if not A:
            return -1
       # list of each column
        with open(A, 'r') as file:
            itemList = file.read().splitlines()
            # list of server name
            col1 = []
            # list of Category
            col2 = []
            # list of App Name
            col3 = []
            # list of App Version
            col4 = []

            # split each row in columns
            for item in itemList:
                if item != '':
                    first, second, third, fourth = item.split(',')
                    col1.append(first.strip())
                    col2.append(second.strip())
                    col3.append(third.strip())
                    col4.append(fourth.strip())

            # Unique App
            col3List = list(set(col3))
            # print(col3List)

            # dictionary of apps and their version
            nameVersionList = {}
            for i in range(len(col3List)):

                version = '0'
                for row in range(len(col3)):
                    if col3[row] == col3List[i]:

                        if version < col4[(row)]:
                            version = col4[row]
                            nameVersionList.update({col3List[i] : version})

            # Server name
            serverLowerVersionList = []

            # Older version
            for key, value in nameVersionList.items():
                lowServer = ''
                lowRow = 0
                lowCount = 0

                # count number of the same version
                for row in range(len(col3)):
                    if col3[row] == key:
                        lowCount += 1

                # Multiple apps having older version
                for row in range(len(col3)):
                    if col3[row] == key:
                        if col4[row] != value:
                            serverLowerVersionList.append(col1[row])

                # Unique servers name
            serverLowerVersonUniqueNameList = list(set(serverLowerVersionList))

            for servername in serverLowerVersonUniqueNameList:
                print(servername)

# Test cases
s = Solution()
A = 'serverlist.txt'
s.serverOutdated(A)
