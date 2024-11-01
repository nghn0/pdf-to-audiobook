import PyPDF2
from gtts import gTTS


reader = PyPDF2.PdfReader('story.pdf')
text = ""
for i in range(0, len(reader.pages)):
    text = text + reader.pages[i].extract_text()


tts = gTTS(text, lang='en', tld='co.in')
file_name = input("Enter the file name to be saved: ")
print("File is being rendered......")
tts.save(f"{file_name}.mp3")
print("File Saved")
