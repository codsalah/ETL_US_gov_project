#!/bin/bash

# Define the start time for the entire process
start_time=$(date +%s)

# Print the start time
echo "Starting the process at $(date)"

# Run merge_csvs.py and measure the time taken
echo "Running merge_csvs.py..."
merge_start_time=$(date +%s)
python3 merge_csvs.py
merge_end_time=$(date +%s)
merge_duration=$((merge_end_time - merge_start_time))
echo "merge_csvs.py completed in $merge_duration seconds."

# Run exploration.py and measure the time taken
echo "Running exploration.py..."
exploration_start_time=$(date +%s)
python3 exploration.py
exploration_end_time=$(date +%s)
exploration_duration=$((exploration_end_time - exploration_start_time))
echo "exploration.py completed in $exploration_duration seconds."

# Print the total time for the entire process
end_time=$(date +%s)
total_duration=$((end_time - start_time))
echo "Total process completed in $total_duration seconds."
