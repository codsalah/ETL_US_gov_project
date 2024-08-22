#!/bin/bash

# Check if the output directory exists
if [ ! -d "$1" ]; then
  echo "Output directory $1 does not exist. Creating it now."
  mkdir -p "$1"
fi

# Loop through each JSON file provided as arguments
# Skip the first argument (output directory)
for json_file in "${@:2}"; do
  # Generate a timestamp for unique output filenames
  timestamp=$(date +"%Y%m%d_%H%M%S")
  
  # Extract the base name of the JSON file (without extension)
  base_name=$(basename "$json_file" .json)
  
  # Define the output CSV file name
  output_file="${base_name}_${timestamp}.csv"

  # Measure start time
  start_time=$(date +%s)

  # Run the Python script with the current JSON file
  python3 main.py -i "$json_file" -o "$1" -f "$output_file" -u

  # Measure end time
  end_time=$(date +%s)
  
  # Calculate elapsed time
  elapsed_time=$((end_time - start_time))

  # Print the result
  echo "Processed $json_file in $elapsed_time seconds. Output saved to $1/$output_file"
done
