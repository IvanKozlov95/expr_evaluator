# constants
operators = ['+', '-', '*', '/', '%', '^']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_precedence(op):
	if op == '-' or op == '+':
		return 13
	elif op == '*' or op == '/' or op == '%':
		return 14
	elif op == '^':
		return 15
	return -1

def opcmp(op1, op2):
	return get_precedence(op1) - get_precedence(op2)

def tokenize(input):
	tokens = input.split(' ')
	for token in tokens:
		for c in token:
			if c not in numbers and c not in operators and c not in "()":
				raise Exception("Invalid symbol '{}'".format(c))
	return tokens

def infix_to_postfix(infix):
	sign = 1
	rpn = []
	stack = []

	for idx, token in enumerate(infix):
		if token in operators:
			while len(stack) > 0 and opcmp(stack[-1], token) >= 0:
				rpn.append(stack.pop())
			stack.append(token)
			lastop = True
		elif token == '(':
			stack.append(token)
		elif token == ')':
			while stack[-1] != '(':
				rpn.append(stack.pop())
			stack.pop()
			lastop = False
		else:
			rpn.append(str(sign * int(token)))
			sign = 1
			lastop = False

	while len(stack) != 0:
		rpn.append(stack.pop())

	return rpn
