import unittest
from hw1part2 import *

class TestHW1Part2(unittest.TestCase):
	"""
	Part2: Web scraping and data collection
	"""

	def test_location_search_params(self):
		"location_search_params: Correct implementation"
		api_key = "test_api_key_xyz"
		location = "Chicago"
		url, headers, url_params = location_search_params(api_key, location, offset=0)
		expected_url = 'https://api.yelp.com/v3/businesses/search'
		self.assertTrue(url == expected_url, msg="API URL does not match")
		auth = headers.get("Authorization")
		self.assertTrue(auth is not None and auth == "Bearer {}".format(api_key), "Authorization Invalid")
		self.assertTrue(url_params.get("offset") == 0, "Keyword args not included in url params")
		self.assertTrue(url_params.get("location") == "Chicago", msg="Location not included in API request")
		# Add more tests

	def test_paginated_restaurants_theaters_search_requests(self):
		"paginated_theater_search_requests: Correct implementation"
		api_key = "test_api_key_xyz"
		location = "Chicago"
		all_theaters_requests = paginated_restaurants_theaters_search_requests(api_key, location, 35)
		self.assertTrue(len(all_theaters_requests) == 3, msg="Incorrect number of pages")
		# offsets = [0, 10, 20, 30]
		for i, request in enumerate(all_theaters_requests):
			self.assertTrue(request[0] == "https://api.yelp.com/v3/businesses/search", msg="API URL does not match")
			self.assertTrue((request[2].get("categories") == "restaurants,movietheaters") or (request[2].get("categories") == "movietheaters,restaurants"), msg="Missing or invalid url parameter")

		all_theaters_requests = paginated_restaurants_theaters_search_requests(api_key, location, 101)
		self.assertTrue(len(all_theaters_requests) == 7, msg="Incorrect number of pages")
		# Add more tests

	# You can add other test cases








