import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2

def read_pdf(pdf_path):
    story = open(pdf_path, "rb")
    pdfreader = PyPDF2.PdfReader(story)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # İsterseniz burada sesi değiştirebilirsiniz=voices[1] erkek sesi...

    for page_number in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_number]
        writing = page.extract_text()
        engine.say(writing)
        engine.runAndWait()

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        read_pdf(file_path)

# TKinter arayüzü
root = tk.Tk()
root.title("PDF Okuyucu")
root.geometry("300x100")

select_button = tk.Button(root, text="PDF Dosyası Seç", command=select_pdf)
select_button.pack(pady=20)

root.mainloop()
