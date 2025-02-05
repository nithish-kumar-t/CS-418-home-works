import unittest
from hw1part1 import *
import pandas as pd
import numpy as np

class TestHour(unittest.TestCase):
	def test_hour(self):
		ser = pd.Series([1030.0, 1259.0, np.nan, 2475], dtype='float64')
		self.assertTrue(extract_hour(ser).equals(pd.Series([10, 12, np.nan, np.nan], dtype='float64')))



class TestMinute(unittest.TestCase):
	def test_minute(self):
		ser = pd.Series([1030.0, 1259.0, np.nan, 2475], dtype='float64')
		self.assertTrue(extract_mins(ser).equals(pd.Series([30, 59, np.nan, np.nan], dtype='float64')))


class TestMinOfDay(unittest.TestCase):
	def test_minofday(self):
		ser = pd.Series([1303, 1200], dtype='float64')
		self.assertTrue(convert_to_minofday(ser).equals(pd.Series([783, 720], dtype='float64')))


class TestTimeDiff(unittest.TestCase):
	def test_timediff(self):
		sched = pd.Series([1303, 1210], dtype='float64')
		actual = pd.Series([1304, 1215], dtype='float64')
		self.assertTrue(calc_time_diff(sched, actual).equals(pd.Series([1, 5], dtype='float64')))
