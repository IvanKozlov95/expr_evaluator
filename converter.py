#!/usr/local/bin/python

import os
import sys

if len(sys.argv) != 2:
	print('Usage: ./converter.py [infix expression]')
	sys.exit()

infix = sys.argv[1]

# operators
operators = ['+', '-', '*', '/', '%', '^']
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

for token in infix:
	if token == ' ':
		continue
	if token in operators:
		while len(stack) > 0 and opcmp(stack[-1], token) >= 0:
			rpn.append(stack.pop())
		stack.append(token)
	elif token == '(':
		stack.append(token)
	elif token == ')':
		while stack[-1] != '(':
			rpn.append(stack.pop())
		stack.pop()
	else:
		rpn.append(token)
while len(stack) != 0:
	rpn.append(stack.pop())

for el in rpn:
	puts(el + ' ')
print()