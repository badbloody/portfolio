start_number = 1
end_number = 29

# Generate the strings and store them in a list
image_strings = [f'"{f}"' for f in [f"image{i}.png" for i in range(start_number, end_number + 1)]]

# Specify the output file name
output_file = "image_strings.txt"

# Write the strings to the output file
with open(output_file, "w") as file:
    for image_string in image_strings:
        file.write(image_string + ",\n")