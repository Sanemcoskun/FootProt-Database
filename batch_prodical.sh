#!/bin/bash

# Define the main directory
input_dir="path/to/input/directory"
output_dir="path/to/output/directory"

# Find all .fa files in the input directory and process them with Prodigal
find "$input_dir" -name "*.fa" | while read file
do
    base=$(basename "$file" .fa)
    prodigal -i "$file" -o "$output_dir/${base}.gbk" -a "$output_dir/${base}_proteins.faa"
done

