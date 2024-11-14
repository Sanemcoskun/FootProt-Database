import os

# source file and new target file
source_file = r"path/to/source/directory"  # Folder containing the FAA files
target_file = r"path/to/target/directory"  # Folder where filtered files will be saved

# If the target folder does not exist, create it
if not os.path.exists(target_file):
    os.makedirs(target_file)

# Iterate through the files in the source directory
for file in os.listdir(source_file):
    if file.endswith(".faa"):  # Only process .faa files
        input_file = os.path.join(source_file, file)
        output_file = os.path.join(target_file, file)

        with open(input_file, 'r') as file_content, open(output_file, 'w') as new_file:
            write_line = False
            for line in file_content:
                if line.startswith(">"):  # Find the header line
                    next_line = next(file_content)
                    if "*" not in next_line:  # If the next line doesn't contain '*' write it
                        new_file.write(line)
                        new_file.write(next_line)

print("All .faa files were successfully filtered and saved in the destination folder.")

