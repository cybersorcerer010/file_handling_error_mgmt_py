# **File Handling and Error Management in Python**

This repository contains Python programs designed to demonstrate efficient file handling and robust error management.

---

### 🖋️ File Read & Write
A program that:
- Reads the content of a user-provided file.
- Applies a modification (e.g., converts text to uppercase).
- Saves the modified content into a new file.

## Example
```python
❯ python file_read_write.py 
Enter the input filename: Hello.txt
Enter the output filename: Hello_World.txt
Modified content successfully written to Hello_World.txt
```

### 🧪 Error Handling
A program that:
- Asks for a filename from the user.
- Handles common errors, such as missing files, permission issues, or invalid file operations.
- Provides meaningful error messages to guide the user.

## Example
```python
❯ python error_handling.py 
Enter the filename to read: Hello.txt
File content:
Hello World!!!
```

```python
❯ python error_handling.py 
Enter the filename to read: Hellos.txt
Error: The file 'Hellos.txt' does not exist.
```

---
