
'''
Sort a stack. Max one stack of auxiliary space allowed, the only allowed operations in the stack are empty(), top(), pop().
'''

def createStack():
    stack = []
    return stack

def isEmpty(stack):
	return len(stack) == 0

# 1: Function is being used for creating a stack (use case purpose).
# Here, push() operation is not being used in main solution.
def push(stack, item):
	stack.append(item)

def pop(stack):
	if isEmpty(stack):
		print("UnderFlow")
		return
	else:
		return stack.pop()

def top(stack):
	if isEmpty(stack):
		return -1
	else:
		return stack[-1]

# 2: Function is being used for use case purpose.
# Here, push() operation is not being used in main solution.
def sortedInsert(stack, x):
	if isEmpty(stack):
		push(stack, x)
		return

	if top(stack) <= x:
		push(stack, x)

	else:
		temp = pop(stack)
		sortedInsert(stack, x)
		push(stack, temp)

def sortstack(stack):
	if isEmpty(stack):
		return
	else:
		temp = pop(stack)
		sortstack(stack)
		sortedInsert(stack, temp)

if __name__ == '__main__':
    s = createStack()
    push(s, '4')
    push(s, '7')
    push(s, '2')
    push(s,	'3')
    push(s, '1')

# prints input stack
    print(s)

# prints output - the sorted-stack
    sortstack(s)
    print(s)

