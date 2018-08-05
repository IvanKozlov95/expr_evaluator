from stack import Stack
from const import operators, numbers

class Converter:

	@staticmethod
	def infix_to_postfix(infix):
		rpn = []
		stack = Stack()

		for idx, token in enumerate(infix):
			if token in operators:
				while stack.Length() > 0 and Converter.opcmp(stack.peek(), token) >= 0:
					rpn.append(stack.pop())
				stack.push(token)
			elif token == '(':
				stack.push(token)
			elif token == ')':
				while stack.peek() != '(':
					rpn.append(stack.pop())
				stack.pop()
			else:
				rpn.append(token)

		while not stack.isEmpty():
			rpn.append(stack.pop())
		return rpn

	@staticmethod
	def incorrect_token(token, pos):
		raise Exception("Incorrect token '{}' at pos {}".format(token, pos))

	@staticmethod
	def opcmp(op1, op2):
		return Converter.get_precedence(op1) - Converter.get_precedence(op2)

	@staticmethod
	def get_precedence(op):
		if op == '-' or op == '+':
			return 13
		elif op == '*' or op == '/' or op == '%':
			return 14
		elif op == '^':
			return 15
		return -1