import io, time, json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


def retrieve_html(url):
    """
    Return the raw HTML at the specified URL.

    Args:
        url (string): 

    Returns:
        status_code (integer):
        raw_html (string): the raw HTML content of the response, properly encoded according to the HTTP headers.
    """
    
    [YOUR CODE HERE]

def location_search_params(api_key, location, **kwargs):
    """
    Construct url, headers and url_params. Reference API docs (link above) to use the arguments
    """
    # What is the url endpoint for search?
    url = [YOUR CODE HERE]
    # How is Authentication performed?
    headers = [YOUR CODE HERE]
    # SPACES in url is problematic. How should you handle location containing spaces?
    url_params = [YOUR CODE HERE]
    # Include keyword arguments in url_params
    [YOUR CODE HERE]
    
    return url, headers, url_params


 def paginated_restaurant_search_requests(api_key, location, total):
    """
    Returns a list of tuples (url, headers, url_params) for paginated search of all restaurants
    Args:
        api_key (string): Your Yelp API Key for Authentication
        location (string): Business Location
        total (int): Total number of items to be fetched
    Returns:
        results (list): list of tuple (url, headers, url_params)
    """
    # HINT: Use total, offset and limit for pagination
    # You can reuse function location_search_params(...)
    [YOUR CODE HERE]
    
#     return 

def parse_api_response(data):
    """
    Parse Yelp API results to extract restaurant URLs.
    
    Args:
        data (string): String of properly formatted JSON.

    Returns:
        (list): list of URLs as strings from the input JSON.
    """
    
    [YOUR CODE HERE]


def parse_page(html):
    """
    Parse the reviews on a single page of a restaurant.
    
    Args:
        html (string): String of HTML corresponding to a Yelp restaurant

    Returns:
        tuple(list, string): a tuple of two elements
            first element: list of dictionaries corresponding to the extracted review information
            second element: URL for the next page of reviews (or None if it is the last page)
    """
    soup = BeautifulSoup(html,'html.parser')
    url_next = soup.find('link',rel='next')
    if url_next:
        url_next = url_next.get('href')
    else:
        url_next = None

    reviews = soup.find_all('div', itemprop="review")
    reviews_list = []
    # HINT: print reviews to see what http tag to extract
    [YOUR CODE HERE]
        
    return reviews_list, url_next

# 4% credits
def extract_reviews(url, html_fetcher):
    """
    Retrieve ALL of the reviews for a single restaurant on Yelp.

    Parameters:
        url (string): Yelp URL corresponding to the restaurant of interest.
        html_fetcher (function): A function that takes url and returns html status code and content
        

    Returns:
        reviews (list): list of dictionaries containing extracted review information
    """
    reviews = []
    [YOUR CODE HERE]
    code, html = html_fetcher(url)
    # HINT: Use function `parse_page(html, url)` multiple times until no next page exists
    [YOUR CODE HERE]
    
    return reviews