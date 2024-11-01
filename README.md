# PDF to Audio Converter

## Description
A Python application that extracts text from a specified PDF file and converts it into an audio file using the Google Text-to-Speech service. Users can enter a desired file name for the output audio, and the application saves the audio in MP3 format.

## Features
- **Text Extraction**: Reads and extracts text from PDF files using PyPDF2.
- **Audio Conversion**: Utilizes gTTS to convert the extracted text into speech.
- **File Naming**: Prompts users to input the desired name for the output audio file.
- **Simple Interface**: Easy to use with a straightforward command-line interface.

## Technologies
- **PDF Handling**: PyPDF2 library for reading and extracting text from PDF files.
- **Text-to-Speech**: gTTS library for converting text into spoken audio.
- **Python**: The application is built using Python for easy execution and installation.

## Usage
1. Ensure that the required libraries (PyPDF2 and gTTS) are installed in your Python environment.
2. Place the PDF file you want to convert in the same directory as the script.
3. Run the application, and enter the desired file name when prompted.
4. The application will extract the text and save it as an MP3 audio file.

## Notes
This project provides a simple solution for converting text from PDF documents into audio format. It showcases how to work with PDF files and utilize text-to-speech capabilities in Python, making it an excellent resource for learning about file handling and audio processing in Python applications.
