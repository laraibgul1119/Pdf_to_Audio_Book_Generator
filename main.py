import pyttsx3
import  PyPDF2
from tkinter.filedialog import *


# Read a file name
book = askopenfilename()

# IT will read the data of pdf and store it in pdfReader
pdfReader = PyPDF2.PdfReader(book)

# This will return the page number of page
pages = len(pdfReader.pages)

# Read all pages from first to specified
for num in range(0,pages):
    # Read the page of specific page number
    page = pdfReader.pages[num]

    # Convert the text of page into string
    text = page.extract_text()

    player = pyttsx3.init()
    voices = player.getProperty('voices')
    player.setProperty('voice',voices[1].id)
    player.say(text)
    player.runAndWait()
    player.stop()
    



