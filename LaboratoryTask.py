import argparse
import re

parser = argparse.ArgumentParser(description='File to read')
parser.add_argument('FileDir',type = str,help='File directory')
arg = parser.parse_args()
words = []
sentenses =[]
numbers = []

try:
     with open(arg.FileDir,'r',encoding="utf-8") as file:
            fileContent = file.read()

            print("количество символов с пробелами: ",len(fileContent))

            fileContentNoSpaces = fileContent.replace(" ",'')
            print("количество символов без пробелов: ",len(fileContentNoSpaces))

            words=re.split(r"[.,-/?! ]",fileContent) 
            for word in words:
                   if word == '':
                          words.pop(words.index(word))
            print(len(words))

            sentenses=re.split(r"[.?!]",fileContent) 
            for word in sentenses:
                   if word == '':
                          sentenses.pop(sentenses.index(word))                     
            print(len(sentenses))

            numbers=re.findall(r'\b[1-9]+\b',fileContent)                          
            print(len(numbers))
                       
except FileNotFoundError:
        print(f"Ошибка: Файл '{dir}' не найден.")
except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
       
    