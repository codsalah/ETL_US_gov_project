# utils/helpers.py

import pandas as pd
from datetime import datetime

def shorten_url(url):
    """
    Shortens a URL by extracting the main domain part.
    """
    # Return None if the url is null
    if pd.isna(url):
        return None
    # Get only the URL eg. www.google.com 
    try:
        parts = url.split('/')
        return parts[2] if len(parts) > 2 else url
    # If not possible return the whole URL
    except Exception:
        return url

def extract_latitude_longitude(value):
    """
    Extracts latitude and longitude from a list.
    """
    # Latitude is the first, longitude is the last
    # Isinstance Insure input is a list before attempting to extract latitude, longitude
    if isinstance(value, list) and len(value) == 2:
        return value[0], value[1]
    return None, None

# timestamp = 1609459200  # Corresponds to 2021-01-01 00:00:00 UTC
def convert_timestamp(timestamp, keep_unix=False):
    """
    Converts UNIX timestamp to human-readable format or keeps it in UNIX format.
    
    Parameters:
    - timestamp (int): The UNIX timestamp to be converted.
    - keep_unix (bool, optional): A flag indicating whether to keep the timestamp in UNIX format.
      - If True, the function returns the timestamp unchanged.
      - If False, the function converts the timestamp to a human-readable 'YYYY-MM-DD HH:MM:SS' . Default is False.
    """
    if keep_unix:
        return timestamp
    else:
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# used to get only the first word instead of full OS        
def extract_first_word(operating_sys):
    """
    Extracts the first word from the operating system string.
    """
    if operating_sys:
        return operating_sys.split()[0]
    return None
