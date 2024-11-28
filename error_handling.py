"""
Error Handling

This script prompts the user for a filename to read. It attempts to open the file using UTF-8 encoding.
If the file is successfully opened, its content is printed. If any error occurs during this process,
appropriate error messages are displayed to the user.

Common errors handled:
    - FileNotFoundError: The file does not exist.
    - PermissionError: The file cannot be read due to permission issues.
    - UnicodeDecodeError: The file contains characters that cannot be decoded using UTF-8.

Usage:
    Run the script and provide a filename when prompted.

Example:
    Enter the filename to read: input.txt
    File content:
    This is the content of the file.
"""

filename = input("Enter the filename to read: ")

try:
    # Specify encoding explicitly to ensure compatibility across systems
    with open(filename, 'r', encoding='utf-8') as file:
        print("File content:")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
except UnicodeDecodeError:
    print(f"Error: The file '{filename}' cannot be decoded using UTF-8 encoding.")
except OSError as e:
    print(f"Error: Operating system error occurred: {e}")
