#!/usr/local/bin/python

import os
import sys

DEBUG = 1
test = "(12 + -2)"
operators = ['+', '-', '*', '/', '%', '^']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def tokenize(input):
	result = []
	tokens = input.split(' ')
	for token in tokens:
		# if len(token) is 1:
		# 	result.append(token)
		# 	continue
		i = 0
		while i < len(token):
			c = token[i]
			if c in numbers:
				# token[0:len(token)]
				tail = token[i:]
				for j in range(0, len(tail)):
					if tail[j] not in numbers:
						break
				if j is len(tail) - 1 and tail[j] in numbers:
					j += 1
				result.append(token[i:i+j])
				i += j
			else:
				result.append(c)
				i += 1
	return result


if DEBUG is 0:
	if len(sys.argv) != 2:
		print('Usage: ./converter.py [infix expression]')
		sys.exit()
	infix = tokenize(sys.argv[1])
else:
	infix = tokenize(test)

stack = []
rpn = []

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

def puts(msg):
	print(msg, end='', flush=True)

lastnumber = False
sign = 1
for token in infix:
	if token == '-' or token == '+' and lastnumber is False:
		sign = -1 if token == '-' else 1
		continue
	if token in operators:
		while len(stack) > 0 and opcmp(stack[-1], token) >= 0:
			rpn.append(stack.pop())
		stack.append(token)
		lastnumber = False
	elif token == '(':
		stack.append(token)
	elif token == ')':
		while stack[-1] != '(':
			rpn.append(stack.pop())
		stack.pop()
	else:
		rpn.append(str(sign * int(token)))
		sign = 1
		lastnumber = True

while len(stack) != 0:
	rpn.append(stack.pop())

for el in rpn:
	puts(el + ' ')
print()