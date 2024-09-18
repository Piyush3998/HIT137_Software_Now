import os
import pandas as pd

csv_folder_path = r"C:\Users\piyus\OneDrive\Documents\SEMESTER--2\HIT137--SOFTWARE NOW\Assignment_2"
output_text_file="output.txt"

with open(output_text_file, 'w') as outfile:
    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            file_path=os.path.join(csv_folder_path,filename)


            df=pd.read_csv(file_path)

            csv_text=df.to_string(index=False)

            outfile.write(f"Contents of {filename}:n\n")
            outfile.write(csv_text)
            outfile.write("n\n\" + ="*50 + "\n\n")


print(f"All CSV files have been successfully written to {output_text_file}")