# PDF Merger Script

## Overview

The PDF Merger Script is a Python utility that enables you to effortlessly merge multiple PDF files into a single PDF document. It utilizes the PyPDF2 library for handling PDF operations, and it adds a touch of visual flair with a stylish banner generated using the pyfiglet library.

## Features

- Merge multiple PDF files into a single PDF.
- Interactive command-line interface.
- Colorful banner for an attractive output.

## Requirements

- Python 3.x
- PyPDF2 library
- pyfiglet library
- colorama library

## Installation

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/deepz2609/pdf_merger.git
2. Navigate to the cloned directory:
   ```sh
   cd pdf_merger 
3. Install the required libraries using pip:
    ```sh
    pip install PyPDF2 pyfiglet colorama

## Usage 
1. Open a terminal or command prompt
2. Navigate to the directory where the `pdf_merger.py` script is located.
3. Run the script:
    ```sh
    python pdf_merger.py
4. Follow the prompts to provide the necessary information:
   - Enter the number of PDF files to merge.
   - Enter the file paths/names for each PDF file.
   - Enter the name of the final merged PDF file (including the ".pdf" extension).
5. The script will merge the PDF files and create the final merged PDF.

## Example
Here's an example of how the script works:
```yaml
$ python pdf_merger.py
    ____  ____  ______   __  _____________  ________________ 
   / __ \/ __ \/ ____/  /  |/  / ____/ __ \/ ____/ ____/ __ \
  / /_/ / / / / /_     / /|_/ / __/ / /_/ / / __/ __/ / /_/ /
 / ____/ /_/ / __/    / /  / / /___/ _, _/ /_/ / /___/ _, _/ 
/_/   /_____/_/      /_/  /_/_____/_/ |_|\____/_____/_/ |_|  

[+]Enter the number of pdf: 2
[+]Enter the 1 pdf file path/name: input1.pdf
[+]Enter the 2 pdf file path/name: input2.pdf
[+]Enter the final pdf name(with .pdf extension): merged_output.pdf

merged_output.pdf has been created successfully!


  
