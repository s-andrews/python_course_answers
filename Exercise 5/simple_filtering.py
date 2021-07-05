#!python
from pathlib import Path

input_file = "cancer_stats.csv"
output_file = "filtered_cancer_stats.csv"

base_folder = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data")

with open(base_folder/input_file) as infile:
    headers = []
    with open(base_folder/output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            data = line.split(",")
            if not headers:
                data.extend(["Male Survival","Female Survival"])
                headers = data
                print(",".join(headers),file=outfile)
                continue

            # Skip cancers only one sex can get
            if data[2] == "NA" or data[3] == "NA":
                continue

            # Convert the numbers to actual numbers
            for i in range(2,6):
                data[i] = float(data[i])

            # Calculate the values
            male_survival = (data[2]-data[4])/data[2]
            female_survival = (data[3]-data[5])/data[3]

            if female_survival > male_survival:
                print(f"Female survival better in {data[1]}: {female_survival:.2f} vs {male_survival:.2f}")
                data.extend([male_survival,female_survival])
                for i in range(len(data)):
                    data[i] = str(data[i])
                
                print(",".join(data),file=outfile)