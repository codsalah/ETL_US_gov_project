#!/bin/bash

# Check if the output directory exists
if [ ! -d "$2" ]; then
  echo "Output directory $2 does not exist. Creating it now."
  mkdir -p "$2"
fi

# Loop through each JSON file provided as arguments
for json_file in "$@"; do
  # Skip the first argument (output directory)
  if [ "$json_file" != "$2" ]; then
    # Generate a timestamp
    timestamp=$(date +"%Y%m%d_%H%M%S")

    # Define the output CSV file name
    output_file="$2/transformed_data_${timestamp}.csv"

    # Measure start time
    start_time=$(date +%s)

    # Run the Python script
    python main.py -i "$json_file" -o "$2" -u

    # Measure end time
    end_time=$(date +%s)
    
    # Calculate elapsed time
    elapsed_time=$((end_time - start_time))

    # Print the result
    echo "Processed $json_file in $elapsed_time seconds. Output saved to $output_file"
  fi
done
