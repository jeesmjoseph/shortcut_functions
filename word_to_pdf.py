# Function to convert a word document to PDF in mac and windows
import logging
from docx2pdf import convert
import glob
import subprocess

logger = logging.getLogger(__name__)

filepath = input("Enter folder location : ")
doc_list = glob.glob(f'{filepath}/*.docx')
for item in doc_list:
    try:
        convert(item)
    except Exception as e:
        if isinstance(e,NotImplementedError):
            subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', item])
        else:
            logger.error(f"Error converting {item}: {e}")
            raise e