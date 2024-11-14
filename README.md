# FootProt-Database
FoodProt is a specialized database offering protein sequences from over 10,000 genomes across 14 food categories. It provides millions of unique sequences for accurate protein identification and functional analysis of food microbiomes, enhancing metaproteomics studies on food quality and safety.

We used Prodigal to analyze prokaryotic data, and to streamline the process and improve efficiency, we utilized several scripts.
You can go to this [link](https://github.com/hyattpd/Prodigal) to install Prodigal.

1. File_transfer.py<br>
We used this script to gather all the .faa files generated by Prodigal into a single folder. These files, along with the .gbk files, were created during the analysis, but we specifically wanted to consolidate only the .faa files into one directory for easier access and management.

2. Filtered.py<br>
This Python script processes all files in bulk to remove lines starting with the `>` symbol and ending with `*` from each `.faa` file. It scans each `.faa` file in the directory and removes the unwanted lines.
