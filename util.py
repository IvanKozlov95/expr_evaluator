import os
import sys

def get_input():
	if len(sys.argv) != 2:
		print('Usage: ./converter.py [infix expression]')
		sys.exit()
	return sys.argv[1]

def puts(msg):
	print(msg, end='', flush=True)