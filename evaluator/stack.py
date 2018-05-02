class Stack:
	def __init__(self):
		self.stack = []
		pass
	
	def push(self, value):
		self.stack.append(value)
	
	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()
		return None

	def peek(self):
		if not self.isEmpty():
			return self.stack[-1]
		return None

	def isEmpty(self):
		return True if self.Length() is 0 else False

	def Length(self):
		return len(self.stack)
