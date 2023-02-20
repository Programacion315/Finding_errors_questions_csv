import csv
import re

# Define the list of special characters to look for in cells
special_chars = r"""[!@$%^&*()_+`\-=\\{}|[\];:"'<>,.ñ]+"""

# opens the input and output CSV files
with open('vehicles.csv', newline='') as input_file, open('output.csv', mode='w', newline='') as output_file:
    input_reader = csv.reader(input_file)
    output_writer = csv.writer(output_file)

    # processes each row
    for row in input_reader:
        new_row = []

        # processes each cell in the row
        for cell in row:
            # if the cell contains a common ASCII character that is not a letter or a number, add a prefix to the cell
            if re.search(special_chars, cell):
                prefix = ""
                for c in re.findall(special_chars, cell):
                    prefix += f"CHARACTER({c}): "
                if len(cell) > 50:
                    prefix += "MAX50: "
                new_row.append(f"{prefix}{cell}")
            elif len(cell) > 50:
                new_row.append(f"MAX50: {cell}")
            else:
                new_row.append(cell)

        # writes the processed row to the output file
        output_writer.writerow(new_row)