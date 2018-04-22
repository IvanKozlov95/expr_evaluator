#!/usr/local/bin/python

import os
import sys

DEBUG = 0
test = "(-2 + -2)"

if DEBUG is 0:
	if len(sys.argv) != 2:
		print('Usage: ./converter.py [infix expression]')
		sys.exit()

	infix = sys.argv[1]
else:
	infix = test

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

lastnumber = False
sign = 1
for token in infix:
	if token == ' ':
		continue
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