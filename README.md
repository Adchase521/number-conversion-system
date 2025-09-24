# number-conversion-system
# Number Converter Program Documentation

## Overview
This Python program is a web-based Number Converter built using the Flet library. It allows users to convert numbers between Binary, Octal, Decimal, and Hexadecimal systems through an interactive interface.

## Features
- Convert numbers between Binary, Octal, Decimal, and Hexadecimal.
- User-friendly web interface with dropdowns for system selection.
- Error handling for invalid inputs and unsupported conversions.
- Clear button to reset input and result fields.

## How It Works
1. **Input**: User enters a number and selects the source and target number systems.
2. **Conversion**: The program converts the input to Decimal, then to the target system.
3. **Output**: The result is displayed. Errors are shown for invalid input.
4. **Clear**: Resets the input and result fields.

## Technologies Used
- Python 3.13
- Flet library

## How to Run
1. Ensure Python 3.13 and Flet are installed.
2. Run the program:
   ```
   C:/Users/Axel.C/AppData/Local/Programs/Python/Python313/python.exe main.py
   ```
3. Open your browser and go to `http://localhost:5000`.

## Main Components
- `main(page: ft.Page)`: Sets up the UI and conversion logic.
- Dropdowns for selecting number systems.
- Conversion function for processing input and displaying results.
- Error handling for invalid numbers and system selection.

## Error Handling
- Invalid input or unsupported conversions display a user-friendly error message.

## Author
- Axel.C

---
