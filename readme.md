# Dark Mode Converter

## Description
This Python script converts PDFs and images in a specified input folder to dark mode, making them easier on the eyes, especially in low-light conditions. The script automatically processes all PDFs, PNGs, JPEGs, and JPGs in the `input` folder and saves the dark mode versions in the `output` folder.

## Setup
1. **Clone the Repository**: Clone this repository to your local machine or download the files.

2. **Anaconda Environment**:
   - If you're using Anaconda, make sure your environment is set up and activated. 
   - If `conda` is not initialized for `cmd.exe`, open the Anaconda Prompt and run `conda init cmd.exe`.

3. **Add Anaconda to PATH**:
   - To run the script directly from the command line, add Anaconda to your PATH environment variable. 
   - This step is necessary if you plan to use the provided batch file or if you're not using the Anaconda Prompt to run the script.

4. **Install Dependencies**:
   - The script requires Python and the following libraries: `PyMuPDF`, `Pillow`.
   - You can install these libraries using `pip install PyMuPDF Pillow` in your Python environment.

## Running the Script
1. **Input and Output Folders**:
   - Place your PDFs, PNGs, JPEGs, and JPGs in the `input` folder located in the same directory as the script.
   - Processed files will be saved in the `output` folder. The script will create the folder if it doesn't exist. If the folder already exists, the script will ask if you want to overwrite the folder or create new one with a version number.

2. **Using the Python Script**:
   - Navigate to the script's directory.
   - Run the script using `python dark_modefy.py`.

3. **Using the Batch File** (Windows Only):
   - Adjust the batch file with the correct path to your Anaconda environment and the script.
   - Run the batch file by double-clicking it.
   - Here's a template for the batch file:

```bat
@echo off
CALL "path\to\anaconda3\Scripts\conda.bat" activate base
CALL "path\to\python.exe" "path\to\dark_modefy.py"
pause
