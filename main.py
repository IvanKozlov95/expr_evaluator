#!/usr/local/bin/python

from converter import infix_to_postfix, tokenize
from evaluator import eval_rpn
from util import *

DEBUG = 0
test =  "2 --( 2 + * -32 )"

_input = get_input() if DEBUG is 0 else test
rpn = infix_to_postfix(tokenize(_input))
print(eval_rpn(rpn))