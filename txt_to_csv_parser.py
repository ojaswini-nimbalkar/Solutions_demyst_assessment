import csv

def parse_fixed_width_file(fixed_width_file, csv_file, spec):
    with open(fixed_width_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(spec.keys())  # Write header

        for line in infile:
            parsed_line = [
                line[spec[field][0]:spec[field][1]].strip() for field in spec
            ]
            writer.writerow(parsed_line)
            print(parsed_line) #for debugging

# Define the specification for the fixed-width file
spec = {
    'first_name': (0, 10),
    'last_name': (10, 25),
    'address': (25, 55),
    'date_of_birth': (55, 65)
}

# Path to the CSV file
csv_file_path = 'output.csv'
file_path='fixed_width_file.txt'

# Parse the fixed-width file and generate the CSV file
parse_fixed_width_file(file_path, csv_file_path, spec)
print("CSV File saved!\n")
