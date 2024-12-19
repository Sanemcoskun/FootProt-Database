import os

# Specify the directory containing .faa files
directory = r'to/path'  # Windows path

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.faa'):  # Check for .faa extension
        file_path = os.path.join(directory, filename)

        # Create a new filename for the cleaned file
        output_file_path = os.path.join(directory, f"cleaned_{filename}")

        # Open the file and process its content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(output_file_path, 'w') as output_file:
            for line in lines:
                # Remove the '*' character if it exists, but don't delete the line
                cleaned_line = line.replace('*', '')
                output_file.write(cleaned_line)

        print(f"Removed '*' characters from {filename} successfully.")
