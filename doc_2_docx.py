# Python function to convert a doc file to docx file
import glob
import subprocess


# Libre-Office Linux approach
for doc in glob.iglob("*.doc"):
    subprocess.call(['soffice', '--headless', '--convert-to', 'docx', doc])
