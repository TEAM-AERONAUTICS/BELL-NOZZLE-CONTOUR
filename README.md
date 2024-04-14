# BELL-NOZZLE-CONTOUR

This project aims to generate Bell Nozzle Contours in your respective designing software (e.g., CATIA, ANSYS, etc.).

## Prerequisites

- This code only works on the latest versions of Python.
- **Python Download Link:** [Download Python](https://www.python.org/downloads/)
- Before using this code, please download the following Excel files:

    1. `NOZZLEPARA`: Contains a few nozzle parameters. Make respective changes in it to get your desired nozzle contour.
    
        - After downloading the Excel sheet in your system, copy the file path and replace it with the path already present inside the code (inside the read_excel function).
          
          ```python
          df = read_excel(r'ENTER YOUR FILE PATH HERE!!')
          ```
    
    2. `NOZZLEPTS`: Contains all the coordinates generated from the code.
    
        - Basically, after you run the code, the coordinates generated from the code will be stored in your desired Excel sheet.
        
        - To store in your desired Excel sheet, just replace the file name 'nozzlepts.xls' with your desired one near the last line of code (e.g., `wb.save('example.xls')`).

## Demo Values and Plots

Demo values are given in the Excel sheets (taken from "VDEngineering"), and also the plots obtained from the values are available for reference.

## Note

- Before you run the code, make sure that the following Python packages are installed:
  
    1. Pandas: [Pandas Download](https://pypi.org/project/pandas/#files)
    2. Scipy: [Scipy Download](https://pypi.org/project/scipy/#files)
    3. Matplotlib: [Matplotlib Download](https://pypi.org/project/matplotlib/#files)
    4. Xlwt: [Xlwt Download](https://pypi.org/project/xlwt/#files)

- After downloading the respective packages, open Command Prompt in your system.
- After opening Command Prompt, type `pip install 'package name'` and do this for all the downloaded packages.
  
  Example: `pip install pandas` (excluding double quotes).

