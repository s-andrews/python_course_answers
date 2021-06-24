#!python
import re

file_name_string = """lane1_NoCode_L001_R1.fastq.gz 
lane1_NoIndex_L001_R1.fastq.gz
lane1_NoIndex_L001_R2.fastq.gz
pipeline_processing_output.log
lane7127_ACTGAT_JH25_L001_R1.fastq.gz
lane7127_ACTTGA_E30_1_2_Hap4_24h_L001_R1.fastq.gz
lane7127_AGTTCC_JH14_L001_R1.fastq.gz
lane7127_CGGAAT_JH37_L001_R1.fastq.gz
lane7127_GCCAAT_E30_1_2l_Hap4_log_L001_R1.fastq.gz
lane7127_GGCTAC_E30_1_4_Hap4_48h_L001_R1.fastq.gz
"""

file_names = file_name_string.split("\n")

for filename in file_names:

    # Ignore empty lines
    if not filename:
        continue

    print("Processing",filename)

    # Check we've got the basic structure first
    lane,barcode = filename.split("_")[0:2]

    if not re.match("^lane\d+$",lane):
        print("Doesn't start with lane")
        continue

    if not re.match("^[GATC]+$",barcode):
        print("No valid barcode")
        continue

    # It looks good, now we need the sample name
    # Remove the lane and barcode from the front

    sample_name = re.sub("^lane\d+_[GATC]+_","",filename)

    # Remove the lane, read and suffix from the end
    sample_name = re.sub("_L\d+_R[1234]\.fastq.gz$","",sample_name)

    print(f"From {filename} Sample name is {sample_name}")


