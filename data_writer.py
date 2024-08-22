import pandas as pd

def write_csv(data_frame, output_path):
    """
    Writes the DataFrame to a CSV file at the specified output path.
    Takes a dataframe as input and output path is where it writes
    """
    data_frame.to_csv(output_path, index=False)
    print(f"CSV file saved to: {output_path}")
