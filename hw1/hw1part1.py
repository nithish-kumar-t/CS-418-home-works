import pandas as pd
import numpy as np

# Question 1.1

def extract_hour(time):
    """
    Extracts hour information from military time.
    
    Args: 
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with hour information.  
          Should only take on integer values in 0-23
    """
    [YOUR CODE HERE]
    
def extract_mins(time):
    """
    Extracts minute information from military time
    
    Args: 
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with hour information.  
          Should only take on integer values in 0-59
    """
    [YOUR CODE HERE]

# Question 1.2

def convert_to_minofday(time):
    """
    Converts military time to minute of day
    
    Args:
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with minute of day
    
    Example: 1:03pm is converted to 783.0
    >>> convert_to_minofday(1303.0)
    783.0
    """
    [YOUR CODE HERE]
    
    
def calc_time_diff(x, y):
    """
    Calculates delay times y - x
    
    Args:
        x (float64): array of scheduled time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
        y (float64): array of same dimensions giving actual time
    
    Returns:
        array (float64): array of input dimension with delay time
    """
    
    scheduled = [YOUR CODE HERE]
    actual = [YOUR CODE HERE]
    
    [YOUR CODE HERE]