import unittest

from pyClass import Operations as op

class TestOp(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(op.sum(2,2), 4, "the result is 4")

	def test_sub(self):
		self.assertEqual(op.sub(2,2), 0, "the result is 0")

	def test_mul(self):
		self.assertEqual(op.mul(2,2), 4, "the result is 4")

	def test_div(self):
		self.assertEqual(op.div(4,2), 2, "the result is 2")

	def test_square_root(self):
		self.assertEqual(op.square_root(4), 2, "the result is 2")

if __name__ == '__main__':
	unittest.main()
