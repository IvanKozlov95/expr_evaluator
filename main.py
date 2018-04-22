#!/usr/local/bin/python
from evaluator import evaluator, converter, util

DEBUG = 0
test =  "+"

_input = util.get_input() if DEBUG is 0 else test
rpn = converter.infix_to_postfix(converter.tokenize(_input))
print(evaluator.eval_rpn(rpn))