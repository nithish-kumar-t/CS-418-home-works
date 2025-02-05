import unittest
import sys

if __name__ == '__main__':
	if len(sys.argv) > 2:
		print("Usage: python run_tests_sample.py <part>")
		exit(1)
	if len(sys.argv) == 1:
		suiteName = "tests_sample_{}".format("part1")
	else:
		suiteName = "tests_sample_{}".format(sys.argv[1])
	
	suite = unittest.defaultTestLoader.discover(suiteName)
	unittest.TextTestRunner().run(suite)
    