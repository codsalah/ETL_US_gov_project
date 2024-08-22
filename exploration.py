import pandas as pd

def explore_csv(file_path: str):
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Show the schema of the DataFrame
    print("Schema of the DataFrame:")
    print(df.dtypes)
    
    # Show the first few rows of the DataFrame
    print("\nFirst few rows of the DataFrame:")
    print(df.head())
    
    # Show basic statistics
    print("\nBasic statistics:")
    print(df.describe(include='all'))

if __name__ == "__main__":
    file_path = './merged_output/final_file.csv'  
    explore_csv(file_path)