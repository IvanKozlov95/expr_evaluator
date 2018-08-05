import sys

from interpreter import Interpreter

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename).read()
        interpreter = Interpreter(file)
        interpreter.parse()