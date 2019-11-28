# Replace multiple three occurrences of a character by a single character
import re

def replace(A, char):
	pattern = char + '{3,}'
	A = re.sub(pattern, char, A)
	return A

# test code
# Input:
A = 'aabbabcbbbdbbbbbbbbba'
char = 'b'
print(replace(A, char))

# Output:
## aabbabcbdba
