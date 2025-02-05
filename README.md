# Escort-for-Visually-Challenged

This project provides accessible solutions for visually challenged individuals by leveraging various Python scripts to assist with reading text from images, converting text to speech, and transforming text into CSV format.

## Features

### 1. **Text-to-Speech**
- Converts a given text into speech using the `pyttsx3` library.
- Provides an audio output of the given text, useful for visually impaired users.

### 2. **Image-to-Text**
- Extracts text from images using Optical Character Recognition (OCR) via `pytesseract`.
- Allows users to convert image-based text (like photographs or scanned documents) into readable text.

### 3. **Text-to-CSV**
- Converts semicolon-separated text files into CSV format, making the data more accessible for analysis.
- Helps users transform data into a structured CSV file format for further use.

## Installation

To run these scripts, you'll need Python installed on your system. You also need to install some external libraries.

### Step 1: Install Python (if not already installed)

Download and install Python from [here](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Use the following command to install the required libraries:

```bash
pip install pyttsx3 pytesseract opencv-python Pillow
```

## Usage

### 1. **Text-to-Speech**

This script reads out a predefined text in speech format.

1. Clone the repository:
    ```bash
    git clone https://github.com/FathimaSheerin/Escort-for-Visually-Challenged.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Escort-for-Visually-Challenged
    ```

3. Run the script:
    ```bash
    python text_to_speech.py
    ```

4. The script will read the provided text aloud.

### 2. **Image-to-Text**

This script extracts text from an image using OCR technology.

1. Ensure that you have the image file available on your system.
2. Edit the script to specify the correct image file path:
    ```python
    image_path = 'YOUR_IMAGE_PATH'
    ```

3. Run the script:
    ```bash
    python image_to_text.py
    ```

4. The script will print the extracted text from the image.

### 3. **Text-to-CSV**

This script converts a semicolon-separated text file into a CSV format.

1. Provide the input file path and output file path in the script:
    ```python
    input_file = 'YOUR_INPUT_FILE_PATH'
    output_file = 'YOUR_OUTPUT_FILE_PATH'
    ```

2. Run the script:
    ```bash
    python text_to_csv.py
    ```

3. The script will replace semicolons with commas and save the updated data in CSV format.

## Contributing

Feel free to fork this repository, make improvements, and create pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
