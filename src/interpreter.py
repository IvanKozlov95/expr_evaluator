from stack import Stack
from converter import Converter
from const import operators, numbers

class Interpreter:

	def __init__(self, code):
		self.lines = code.split('\n')
		self.variables = dict()

	def parse(self):
		for line in self.lines:
			tokens = self.parse_line(line)
			if len(tokens) == 3:
				self.evaluate_variable(tokens)
			else:
				self.evaluate(tokens)
		pass

	def parse_line(self, line):
		return line.split(' ')

	def evaluate(self, tokens):
		postfix = Converter.infix_to_postfix(tokens)
		return Evaluator.eval_rpn(postfix, self.variables)

	def evaluate_variable(self, tokens):
		if len(tokens) != 3 or not tokens[0].isalpha() or tokens[1] != '=':
			raise Exception("Incorrect variable assigning at line {}".format(self.lines.index(' '.join(tokens)) + 1))
		self.variables[tokens[0]] = int(tokens[2])


class Evaluator:
	_sum = lambda a, b: a + b
	sub = lambda a, b: a - b
	mul = lambda a, b: a * b
	div = lambda a, b: a / b
	mod = lambda a, b: a % b
	_pow = lambda a, b: pow(a, b)
	operations = [_sum, sub, mul, div, mod, _pow]

	@staticmethod
	def process_op(b, a, op):
		return Evaluator.operations[operators.index(op)](int(a), int(b))

	@staticmethod
	def eval_rpn(rpn, variables):
		stack = Stack()
		for el in rpn:
			if el in operators:
				if stack.Length() < 2:
					raise Exception("Missing an operand")
				res = Evaluator.process_op(stack.pop(), stack.pop(), el)
				stack.push(res)
			else:
				if el in variables:
					stack.push(int(variables[el]))
				else:
					stack.push(el)
		if stack.Length() > 1:
			raise Exception("Missing an operation")
		return stack.pop()