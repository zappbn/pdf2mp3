from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf2mp3(file_path='test.pdf', lang='en'):
    if Path(file_path).is_file() and Path(file_path).suffix=='.pdf':
       #return  'File exists!'
       print(f'[+] Original file: {Path(file_path).name}')
       print('[+] Processing')
       with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
           pages = [page.extract_text() for page in pdf.pages]

       text = ''.join(pages)
       text = text.replace('\n','')
       #with open('text.txt','w') as file:
        #   file.write(text)
       my_audio = gTTS(text=text, lang=lang)
       file_name = Path(file_path).stem
       my_audio.save(f'{file_name}.mp3')
       return f'[+] {file_name}.mp3 saved successfully!\n--- Have a nice day!---'

    else:
        return 'File does not exist'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    lang= input("Enter language: 'en' or 'ru': ")
    print(pdf2mp3(file_path=file_path,lang=lang))


if __name__ == '__main__':
    main()

