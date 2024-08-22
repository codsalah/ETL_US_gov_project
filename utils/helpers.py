# utils/helpers.py

import pandas as pd
from datetime import datetime

def shorten_url(url):
    """
    Shortens a URL by extracting the main domain part.
    """
    if pd.isna(url):
        return None
    try:
        parts = url.split('/')
        return parts[2] if len(parts) > 2 else url
    except Exception:
        return url

def extract_latitude_longitude(value):
    """
    Extracts latitude and longitude from a list.
    """
    if isinstance(value, list) and len(value) == 2:
        return value[0], value[1]
    return None, None

def convert_timestamp(timestamp, keep_unix=False):
    """
    Converts UNIX timestamp to human-readable format or keeps it in UNIX format.
    """
    if keep_unix:
        return timestamp
    else:
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        
def extract_first_word(operating_sys):
    """
    Extracts the first word from the operating system string.
    """
    if operating_sys:
        return operating_sys.split()[0]
    return None
