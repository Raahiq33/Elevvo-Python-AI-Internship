
# Automated File Organizer

## Elevvo Python Programming & AI Internship – Task 3

A Python-based file organization tool that automatically sorts files into folders according to their extensions.

## Features

- Automatically categorizes files by type
- Supports images, PDFs, documents, spreadsheets, videos, audio, archives, and code files
- Prevents overwriting existing files by generating unique filenames
- Displays source and destination paths for every moved file
- Handles empty folders, invalid paths, and file access errors
- Requests user confirmation before moving files

## Technologies Used

- Python
- pathlib
- shutil
- Visual Studio Code

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

    py organizer.py

4. Enter the folder path you want to organize.
5. Type `yes` to confirm.

## Example

Before:

    Test_Files/
    ├── photo.jpg
    ├── report.csv
    └── sample.txt

After:

    Test_Files/
    ├── Images/
    │   └── photo.jpg
    ├── Spreadsheets/
    │   └── report.csv
    └── Documents/
        └── sample.txt

## Testing

- File categorization
- Duplicate filename handling
- Invalid folder path handling

## Safety

Test the program using a sample folder before organizing important files. The program moves files rather than copying them.

## Internship

Elevvo – Python Programming & AI Internship

Task 3: Automated File Organizer
