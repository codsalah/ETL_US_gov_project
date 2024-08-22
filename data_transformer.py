# data_transformer.py
import os
import pandas as pd
from datetime import datetime
from utils.helpers import shorten_url, extract_latitude_longitude, convert_timestamp
from file_reader import read_json_file
from data_writer import write_csv

def transform_data(input_path, output_path, keep_unix=False):
    """
    Transforms JSON data to CSV format and saves it to the specified output path.
    """
    # Read JSON file using file_reader
    data = read_json_file(input_path)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Transformations
    # Extract operating system
    df['operating_sys'] = df['a'].str.extract(r'\(([^)]+)\)')[0]
    
    # Extract web browser
    df['web_browser'] = df['a'].str.extract(r'^(\S+)/')[0]
    
    # Shorten URLs
    df['from_url'] = df['r'].apply(shorten_url)
    df['to_url'] = df['u'].apply(shorten_url)
    
    # Extract city, latitude, and longitude
    df['city'] = df['cy']
    
    # Apply extraction function for latitude and longitude
    df[['latitude', 'longitude']] = df['ll'].apply(lambda x: pd.Series(extract_latitude_longitude(x)))
    
    # Convert timestamps
    df['time_in'] = df['t'].apply(lambda x: convert_timestamp(x, keep_unix))
    df['time_out'] = df['hc'].apply(lambda x: convert_timestamp(x, keep_unix))
    
    df['time_zone'] = df['tz']
    
    # Remove NaN values
    df = df[['web_browser', 'operating_sys', 'from_url', 'to_url', 'city', 'latitude', 'longitude', 'time_zone', 'time_in', 'time_out']]
    df = df.dropna()
    
    # Check for duplicates and remove
    df = df.drop_duplicates()
    
    # Output file path
    output_file = os.path.join(output_path, 'transformed_data.csv')
    
    # Save to CSV using data_writer
    write_csv(df, output_file)
    
    print(f"Number of records transformed: {len(df)}")
