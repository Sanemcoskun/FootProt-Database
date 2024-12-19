import os
import subprocess

# Base directory path
base_dir = r"C:/Users/sanem/Downloads/cFMD_mags/cFMD_mags/Categorized_FAA"

# Full path to SeqKit
seqkit_path = r"C:/Users/sanem/Downloads/seqkit_windows_amd64.exe/seqkit.exe"

# Process combined.faa files in each subdirectory
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "combined.faa":
            input_file = os.path.join(root, file)
            output_file = os.path.join(root, "combined_cleaned.faa")
            
            print(f"Processing: {input_file}")
            
            try:
                # Run SeqKit using its full path
                subprocess.run([seqkit_path, "rmdup", "-s", "-o", output_file, input_file], check=True)
                print(f"Cleaned file saved as: {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {input_file}: {e}")
