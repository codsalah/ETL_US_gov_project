# ETL_US_Gov_Project

This project involves an ETL (Extract, Transform, Load) pipeline that processes web browsing data. The main tasks include merging CSV files, exploring data with Pandas, and analyzing distributions.

## Project Overview

### 1. **Data Files**

- **CSV Files:** Input files are located in the `output_directory` folder.
- **Merged CSV File:** The final merged data is saved as `final_file.csv` in the `merged_output` folder.

### 2. **Scripts**

###  `merge_csvs.py`**

Merges multiple CSV files from the `output_directory` into a single CSV file. The merged file is saved to `merged_output/final_file.csv`.

### `exploration.py`**

Reads the merged CSV file and performs data exploration tasks using Pandas. This includes generating statistics and visualizations of the data.

### `file_reader.py`

This module provides functionality for reading data from files.

### `file_writer.py`

This module provides functionality for writing data to files.

### `data_transformer.py`

This module handles data transformation tasks.

### `main.py`

The main entry point of the application that orchestrates the reading, transforming, and writing of data.

### `utils/helpers.py`

This module contains utility functions that assist with transformation tasks in the project.



## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Ensure you have `pandas` and `matplotlib` installed. You can install them using pip:

   ```bash
   pip install pandas matplotlib
   ```

## Usage

### Running the ETL Pipeline

1. **Merge CSV Files**

   Run the `merge_csvs.py` script to merge CSV files:

   ```bash
   python merge_csvs.py
   ```

   This will merge all CSV files from `output_directory` and save the result in `merged_output/final_file.csv`.

2. **Explore the Data**

   Run the `exploration.py` script to perform data exploration:

   ```bash
   python exploration.py
   ```

   This script reads the merged CSV file and performs various data analysis tasks, including generating plots and statistics.

### Automated Execution
To run schedule script use the provided `shedule.sh` script:
```bash
./shedule_bash.sh output_directory usa_gov_click_data4.json usa_gov_click_data5.json  usa_gov_click_data7.json
```

To run both scripts in sequence and measure execution time, use the provided `run_all.sh` script:

```bash
./run_all.sh
```


This script will execute `merge_csvs.py` and `exploration.py`, printing the duration of each script and the total execution time.

## Data Schema

The merged CSV file `final_file.csv` contains the following columns:

- **`web_browser`**: Browser used
- **`operating_sys`**: Operating system
- **`from_url`**: URL from which the user arrived
- **`to_url`**: URL to which the user navigated
- **`city`**: City of the user
- **`latitude`**: Latitude of the user's location
- **`longitude`**: Longitude of the user's location
- **`time_zone`**: Time zone of the user
- **`time_in`**: Timestamp when the user arrived
- **`time_out`**: Timestamp when the user left
