# Importing required libraries
from langchain.llms import OpenAI
from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
import re
from langchain.prompts import PromptTemplate


# Creating a pdf to text extraction function
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfFileReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract information from PDF text

