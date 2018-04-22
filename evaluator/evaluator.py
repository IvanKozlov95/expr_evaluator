operators = ['+', '-', '*', '/', '%', '^']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

_sum = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
mod = lambda a, b: a % b
_pow = lambda a, b: pow(a, b)
operations = [_sum, sub, mul, div, mod, _pow]

def process_op(b, a, op):
	return operations[operators.index(op)](int(a), int(b))

def eval_rpn(rpn):
	stack = []
	for el in rpn:
		if el in operators:
			if len(stack) < 2:
				raise Exception("Missing an operand")
			res = process_op(stack.pop(), stack.pop(), el)
			stack.append(res)
		else:
			stack.append(el)
	if len(stack) > 1:
		raise Exception("Missing an operation")
	return stack.pop()