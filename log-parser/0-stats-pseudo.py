#!/usr/bin/python3
"""
Module: Task 0 - parsing HTTP request logs.
"""

import re

def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    
    Args:
        input_line (str): A line from the HTTP request log.
    
    Returns:
        dict: Dictionary containing extracted information (status code and file size).
    
    Raises:
        ValueError: If the input line does not match the expected format.
    """
    # Define regular expression pattern to extract information from the input line
    # Use regex pattern to match against the input line  
    # Extract relevant information (status code and file size) from the match    
    # Return extracted information as a dictionary    
    # Handle invalid input format by raising a ValueError


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    
    Args:
        total_file_size (int): Total size of files processed so far.
        status_codes_stats (dict): Dictionary containing counts of status codes.
    """
    # Print total file size    
    # Iterate over status code counts and print each one


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates the metrics from a given HTTP request log.
    
    Args:
        line (str): A line from the HTTP request log.
        total_file_size (int): Total size of files processed so far.
        status_codes_stats (dict): Dictionary containing counts of status codes.
    
    Returns:
        int: Updated total file size.
    """
    # Extract information (status code and file size) from the input line using extract_input
    # Update status code counts and total file size
    # Return updated total file size


def run():
    """
    Starts the log parser.
    """
    # Initialize total file size and status code counts
    
    try:
        # Read input lines until interrupted        
        # Update metrics and print statistics after every 10 lines
        
    except KeyboardInterrupt:
        # Print final statistics upon keyboard interruption


if __name__ == "__main__":
    run()
