import pandas as pd
import os
folder_path = './Data'

def merge_csv_files(input_folder: str, output_folder: str, output_file: str):

    os.makedirs(output_folder, exist_ok=True)
    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]  

    if not csv_files:
        print(f"No CSV files found in the folder: {input_folder}")
        return

    # Read and concatenate all CSV files
    df_list = []
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path)
        df_list.append(df)
    
    # Concatenate all dataframes into a single dataframe
    merged_df = pd.concat(df_list, ignore_index=True)

    output_file_path = os.path.join(output_folder, output_file)

    # Save the merged dataframe to a CSV file
    merged_df.to_csv(output_file_path, index=False)
    print(f"Merged CSV file saved to: {output_file_path}")

if __name__ == "__main__":
    input_folder = './output_directory/'
    output_folder = './merged_output/'
    output_file = 'final_file.csv'
    merge_csv_files(input_folder, output_folder, output_file)