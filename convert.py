# Function to convert a line to the desired format
def convert_line(line):
    parts = line.strip().split('\t')
    if len(parts) == 3:
        first_name, last_name, email = parts
        formatted_line = f"{first_name} {last_name} <{email}>"
        return formatted_line
    else:
        return None

# Input and output file paths
input_file_path = 'input.txt'  # Change to your input file path
output_file_path = 'output.txt'  # Change to your desired output file path

# Open the input file and create the output file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        formatted_line = convert_line(line)
        if formatted_line:
            output_file.write(formatted_line + '\n')

print(f"Conversion completed. Results saved in {output_file_path}")
