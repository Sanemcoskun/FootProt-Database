import os
import shutil

# The folder path where the files are located and the new folder path where you want to move them
source_folder = "to/path"  # Write the source folder path here
target_folder = "to/path"    # Write the target folder path here

# If the target folder does not exist, create it
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Check all files in source folder
for file in os.listdir(source_folder):
    if dosya.endswith(".faa"):  # Only select files with .faa extension
        path = os.path.join(source_folder, file)
        shutil.move(path, target_folder)  # Move file to target folder

print("FAA files moved to new folder.")
