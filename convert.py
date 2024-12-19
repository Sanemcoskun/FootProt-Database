import os

def convert_aa_to_faa(directory):
    """
    Converts files with the .aa extension to .faa extension.

    :param directory: Path to the directory containing .aa files.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist.")
        return

    aa_files = [f for f in os.listdir(directory) if f.endswith('.aa')]

    if not aa_files:
        print("No .aa files found in the directory.")
        return

    for file in aa_files:
        aa_path = os.path.join(directory, file)
        faa_path = os.path.join(directory, file.replace('.aa', '.faa'))
        os.rename(aa_path, faa_path)
        print(f"{file} -> {file.replace('.aa', '.faa')} renamed successfully.")

if __name__ == "__main__":
    directory = r"to/path"
    convert_aa_to_faa(directory)
