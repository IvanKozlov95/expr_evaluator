from stack import Stack
from const import operators, numbers

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
