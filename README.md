# ScreenshotGPT

OCR Text Extraction with ChatGPT Integration

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project allows you to extract text from images using OCR (Optical Character Recognition) and integrate it with OpenAI's ChatGPT for interactive conversations. It provides a convenient way to extract information from images and ask the assistant questions based on the extracted text.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install the required dependencies: `pip install pytesseract pillow openai`

## Usage

To use the project, follow these steps:

1. Provide an image containing text.
2. The script will extract the text using OCR.
3. The extracted text will be used as input to the ChatGPT model.
4. The assistant will provide a response based on the given information.

Here's an example code snippet:

```python
import pytesseract
from PIL import Image
import openai

# OCR text extraction code goes here

# ChatGPT integration code goes here 
```

## Examples

Here are a few examples to showcase the functionality of the project:

1. Extracting text from an image containing a handwritten note and asking the assistant for its interpretation.
2. Extracting text from a screenshot of a book summary and asking the assistant for additional details or related recommendations.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. See the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
