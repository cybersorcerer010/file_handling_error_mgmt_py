"""
File Read & Write

This script prompts the user for an input filename and an output filename.
It reads the content of the input file, applies a modification (converts the text to uppercase),
and writes the modified content to the output file.

If the input file does not exist or cannot be read, appropriate error messages are displayed.

Usage:
    Run the script and follow the prompts to provide filenames.

Example:
    Enter the input filename: input.txt
    Enter the output filename: output.txt
    Modified content successfully written to output.txt
"""

# File Read & Write
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

try:
    # Specify encoding explicitly to ensure compatibility across systems
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
        modified_content = content.upper()  # Example modification: Convert text to uppercase
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content) 
    print(f"Modified content successfully written to {output_file}")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except IOError as e:
    print(f"Error: Unable to process the file. ({e})")
except UnicodeDecodeError:
    print(f"Error: The file '{input_file}' cannot be decoded with UTF-8 encoding.")
