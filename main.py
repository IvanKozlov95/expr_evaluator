#!/usr/local/bin/python

from converter import infix_to_postfix, tokenize
from evaluator import eval_rpn
from util import *

DEBUG = 0
test =  "+"

_input = get_input() if DEBUG is 0 else test
rpn = infix_to_postfix(tokenize(_input))
print(rpn)
if len(rpn) is 0:
	print("nothing in rpn")
else:
	print(eval_rpn(rpn))