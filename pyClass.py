import math

class Operations:

	def sum(a1, a2):
		return a1 + a2

	def sub(a1, a2):
		return a1-a2

	def mul(a1, a2):
		return a1*a2

	def div(a1, a2):
		try:
			division = a1/a2
		except ZeroDivisionError:
			return None
		return division

	def square_root(a1):
		try:
			squareRoot = math.sqrt(a1)
		except ValueError:
			return None
		return squareRoot
