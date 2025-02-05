# Convert semicolon-separated text file to CSV
input_file = 'YOUR_INPUT_FILE_PATH'  # Provide the input file path as a string
output_file = 'YOUR_OUTPUT_FILE_PATH'  # Provide the output file path as a string

# Read the file and replace semicolons with commas
with open(input_file, 'r') as file:
    data = file.read()

# Replace semicolons with commas
data = data.replace(';', ',')

# Save the updated data to a new CSV file
with open(output_file, 'w') as file:
    file.write(data)

print("File has been successfully converted to CSV!")
