# Text-to-Speech and Text-to-CSV

This repository contains two Python scripts:

1. **Text-to-Speech**: Demonstrates a basic implementation of text-to-speech conversion using Python's `pyttsx3` library. The script takes a given text and converts it into speech.
2. **Text-to-CSV**: Converts a semicolon-separated text file into a CSV format by replacing semicolons with commas.

## Features

### Text-to-Speech
- Convert text into speech with customizable voice properties.
- Simple and easy-to-use Python script.
- Compatible with different platforms (Windows, Mac, Linux).

### Text-to-CSV
- Convert semicolon-separated text files into CSV files.
- Useful for cleaning and transforming data for further analysis.

## Installation

To run these scripts, you'll need to have Python installed on your system. You also need to install the required libraries for each script.

### Step 1: Install Python (if not already installed)

If you don't have Python installed, download and install the latest version from [here](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Use `pip` to install the required libraries for the **Text-to-Speech** script:

```bash
pip install pyttsx3
``` 

For the **Text-to-CSV** script, no additional dependencies are required, as it uses Python's built-in functions.

## Usage

### Text-to-Speech

1. Clone the repository:
    
    ```bash
    git clone https://github.com/FathimaSheerin/Text-to-Speech-.git
    ```
    
2. Navigate to the project folder:
    
    ```bash
    cd Text-to-Speech-
    ```
    
3. Run the Python script:
    
    ```bash
    python text_to_speech.py
    ```
    
4. The script will read out the provided text aloud.

### Text-to-CSV

1. Clone the repository (if not done already):
    
    ```bash
    git clone https://github.com/FathimaSheerin/Text-to-Speech-.git
    ```

2. Navigate to the project folder:
    
    ```bash
    cd Text-to-Speech-
    ```

3. Edit the `text_to_csv.py` script to specify the input and output file paths.

4. Run the Python script:
    
    ```bash
    python text_to_csv.py
    ```

5. The script will convert the semicolon-separated text file into a CSV file.

## Contributing

Feel free to fork this repository, make improvements, and create pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

