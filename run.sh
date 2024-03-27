#!/bin/bash

# Define the location of the Python script
PYTHON_SCRIPT="hdfs_command.py"

# Define the file to capture the output
OUTPUT_FILE="script_output.txt"

# Execute the Python script and capture the output
python3 "$PYTHON_SCRIPT" > "$OUTPUT_FILE" 2>&1

echo "The output of the Python script has been saved to $OUTPUT_FILE"
