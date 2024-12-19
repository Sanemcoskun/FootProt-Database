import os

# Base directory containing categorized folders
categorized_dir = r"C:\Users\sanem\Downloads\cFMD_mags\cFMD_mags\Categorized_FAA"

# Iterate through each category folder in the base directory
for category in os.listdir(categorized_dir):
    cat_path = os.path.join(categorized_dir, category)
    
    # Check if it's a directory
    if os.path.isdir(cat_path):
        # Find all .faa files in the folder
        faa_files = [f for f in os.listdir(cat_path) if f.endswith('.faa')]
        
        # If there are .faa files, combine them
        if faa_files:
            combined_file = os.path.join(cat_path, "combined.faa")
            with open(combined_file, 'w', encoding='utf-8') as outfile:
                for faa in faa_files:
                    faa_path = os.path.join(cat_path, faa)
                    with open(faa_path, 'r', encoding='utf-8') as infile:
                        # Read each file and append to the combined file
                        outfile.write(infile.read())
                        # Optionally add a newline between files
                        # outfile.write('\n')
            
            print(f"{len(faa_files)} files in the {category} folder were combined into combined.faa.")
        else:
            print(f"No .faa files found in the {category} folder.")
