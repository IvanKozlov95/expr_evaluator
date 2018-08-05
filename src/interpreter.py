from stack import Stack
from const import operators, numbers
from converter import Converter
from evaluator import Evaluator

class Interpreter:

	def __init__(self, code):
		self.lines = code.split('\n')
		self.variables = dict()

	def run(self):
		for line in self.lines:
			tokens = self.parse_line(line)
			res = self.evaluate(tokens)
		return res

	def parse_line(self, line):
		return line.split(' ')

	def evaluate(self, tokens):
		if '=' in tokens:
			self.evaluate_variable(tokens)
		else:
			postfix = Converter.infix_to_postfix(tokens)
			return Evaluator.eval_rpn(postfix, self.variables)

	def evaluate_variable(self, tokens):
		if len(tokens) != 3 or not tokens[0].isalpha() or tokens[1] != '=':
			raise Exception("Incorrect variable assigning at line {}".format(self.lines.index(' '.join(tokens)) + 1))
		self.variables[tokens[0]] = int(tokens[2])
