import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string('C:\\Users\\robmp\\Pictures\\Saved Pictures\\image1.png'))
