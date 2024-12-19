import os
import pandas as pd
import matplotlib.pyplot as plt

# Base directory path
base_dir = r"C:/Users/sanem/Downloads/cFMD_mags/cFMD_mags/Categorized_FAA"

# Output directory path
output_dir = r"to/path"
output_csv = os.path.join(output_dir, "genome_category_summary.csv")
output_plot = os.path.join(output_dir, "genome_analysis_plot.png")

# List to store results
results = []

# Function to count FASTA headers
def count_fasta_headers(file_path):
    with open(file_path, "r") as f:
        return sum(1 for line in f if line.startswith(">"))

# Analyze combined.faa files in each subfolder
for root, dirs, files in os.walk(base_dir):
    if root == base_dir:  # Skip the base directory
        continue
    
    category = os.path.basename(root)  # Extract category name
    total_headers = 0
    total_size = 0
    
    for file in files:
        if file == "combined.faa":
            file_path = os.path.join(root, file)
            headers = count_fasta_headers(file_path)
            total_headers += headers
            total_size += os.path.getsize(file_path)
    
    # Append results
    results.append({"Category": category, "Genome_Count": total_headers, "Total_Size_MB": total_size / (1024 * 1024)})

# Convert results to a DataFrame
df = pd.DataFrame(results)
df = df.sort_values(by="Genome_Count", ascending=False)

# Save results as CSV
df.to_csv(output_csv, index=False)
print(f"Results saved to CSV file: {output_csv}")

# Generate plots
plt.figure(figsize=(14, 6))

# 1. Genome count plot
plt.subplot(1, 2, 1)
plt.bar(df["Category"], df["Genome_Count"], color='steelblue')
plt.title("Genome Count by Category", fontsize=12)
plt.xlabel("Category", fontsize=10)
plt.ylabel("Genome Count", fontsize=10)
plt.xticks(rotation=25, ha="right", fontsize=8)

# 2. Database size plot
plt.subplot(1, 2, 2)
plt.bar(df["Category"], df["Total_Size_MB"], color='orange')
plt.title("Protein Database Size (MB)", fontsize=12)
plt.xlabel("Category", fontsize=10)
plt.ylabel("Size (MB)", fontsize=10)
plt.xticks(rotation=25, ha="right", fontsize=8)

# Save the plots
plt.tight_layout()
plt.subplots_adjust(wspace=0.4)
plt.savefig(output_plot, dpi=300, bbox_inches='tight')  # Save the plot
print(f"Plot saved to file: {output_plot}")

# Show the plot
plt.show()
