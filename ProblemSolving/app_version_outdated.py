'''Find out of Oudated Servers from the list of the servers.

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
    def appVersionOutdated(self, A):
        with open(A, 'r') as file:
            server = []
            lang = []
            app = []
            versionlist = []
            for line in file:
                col1, col2, col3, col4 = line.strip().split(', ')

                server.append(col1)
                lang.append(col2)
                app.append(col3)
                versionlist.append(col4)

            # Unique list of app
            applist = list(set(app))

            # dictionary of apps and their version
            nameVersionlist = {}
            for i in range(len(applist)):
                version = '0'
                for j in range(len(app)):
                    if app[j] == applist[i]:

                        if version < versionlist[j]:
                            version = versionlist[j]
                            nameVersionlist.update({applist[i]: version})

            # print(nameVersionlist)
            serverLowerVersionList = []

            # Older version
            for key, value in nameVersionlist.items():
                count = 0
                # count number of the same version
                for j in range(len(app)):
                    if app[j] == key:
                        count += 1

               # Multiple apps having older version
                for j in range(len(app)):
                    if app[j] == key:
                        if versionlist[j] != value:
                            serverLowerVersionList.append(server[j])

                # Unique servers name
            serverLowerVersonUniqueNameList = list(set(serverLowerVersionList))

            for sname in serverLowerVersonUniqueNameList:
                print(sname)

#  test code
s = Solution()
A = 'serverlist.txt'
s.appVersionOutdated(A)

## Output:
# Server1
# Server2
# Server3
