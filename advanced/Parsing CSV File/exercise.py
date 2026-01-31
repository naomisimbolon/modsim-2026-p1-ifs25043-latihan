import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(BASE_DIR, 'inputfile.csv')
output_path = os.path.join(BASE_DIR, 'outputfile.csv')

with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)

    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            if int(row[0]) > 50:
                writer.writerow(row)