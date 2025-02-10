# LingoSense

LingoSense is a Python-based application designed for language detection and translation. It provides users with the ability to identify languages and translate text efficiently.

## Features

- **Language Detection**: Automatically identify the language of a given text input.
- **Text Translation**: Translate text from one language to another seamlessly.

## Installation

### Clone the Repository:

```bash
git clone https://github.com/Priyanshu23u/LingoSense.git
cd LingoSense
```

### Set Up a Virtual Environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Application:

```bash
python app.py
```

### Access the Web Interface:

Open your web browser and navigate to `http://127.0.0.1:5000/` to use the LingoSense application.

## File Structure

```
LingoSense/
├── templates/                 # HTML templates for the web interface
├── venv/                      # Virtual environment directory
├── Lang_detect_translate.ipynb # Jupyter Notebook for language detection and translation
├── Procfile                   # For deployment configurations
├── app.py                     # Main application script
├── link.txt                   # Contains relevant links or references
└── requirements.txt           # List of dependencies
```

## Dependencies

Ensure the following Python packages are installed:

- **Flask**: For the web framework.
- **Langdetect**: For language detection.
- **Googletrans**: For translation services.

These can be installed using the `requirements.txt` file provided.


