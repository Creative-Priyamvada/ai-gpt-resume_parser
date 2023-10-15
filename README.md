# ai-gpt-resume_parser


# Project Name

Briefly describe your project here.

## Files

This project consists of the following files:

### `calling_chatGPT.py`

This file contains the code responsible for using OpenAI's GPT-4 model for processing text. It includes a function `chatGPT_output` that utilizes the OpenAI API to clean up and format text in a specific way.

```python
import openai
import os

openai.api_key = "Enter your API key here"

def chatGPT_output(resume_text):
    # Function logic goes here


pdf2text.py
This file contains the code for extracting text from a PDF document using the PyPDF2 library. It defines a function pdf_to_text that reads a PDF file and returns the extracted text.





main.py
This file is the main script of the project, and it uses the functions defined in the previous two files. It sets up a Flask web application with an API endpoint for converting PDF documents to text and processing them with the chatGPT_output function.


Usage
Provide instructions on how to use your project, what each file does, and how to set up API keys if necessary.