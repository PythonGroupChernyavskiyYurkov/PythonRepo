
import argparse
import re

def main():
       parser = argparse.ArgumentParser(description='File to read')
<<<<<<< HEAD
       parser.add_argument('file_dir',type = str,help='File directory')
=======
       parser.add_argument('FileDir',type = str,help='File directory')
>>>>>>> dddcb49dee654443653d5abdd37adf0962a34e50
       arg = parser.parse_args()
       words = []
       sentenses = []
       numbers = []

       try:
<<<<<<< HEAD
              with open(arg.file_dir,'r',encoding="utf-8") as file:
                     #Чтение файла в переменную
                     file_content = file.read()

                     #Первый пункт
                     print("количество символов с пробелами: ",len(file_content))

                     fileContentNoSpaces =  file_content.replace(" ",'')
                     print("количество символов без пробелов: ",len(fileContentNoSpaces))

                     #Второй пункт
                     words=re.findall(r"\b[A-z]+\b", file_content) 
                     for word in words:
                            if word == ' ' or word =='':
                                   words.pop(words.index(word))
                     print(f"Количество слов в тексте: {len(words)}")

                     #Третий пункт
                     sentenses=re.split(r"[.?!]", file_content) 
                     for word in sentenses:
                            if word == '':
                                   sentenses.pop(sentenses.index(word))                     
                     print(f"Количество предложений в тексте: {len(sentenses)}")

                     #Четвёртый пункт
                     numbers=re.findall(r'\b[1-9]+\b', file_content)                          
                     print(f"Количество чисел в тексте: {len(numbers)}")
=======
              with open(arg.FileDir,'r',encoding="utf-8") as file:
                     #Чтение файла в переменную
                     fileContent = file.read()

                     #Первый пункт
                     print("количество символов с пробелами: ",len(fileContent))

                     fileContentNoSpaces = fileContent.replace(" ",'')
                     print("количество символов без пробелов: ",len(fileContentNoSpaces))

                     #Второй пункт
                     words=re.split(r"[.,-/?! ]",fileContent) 
                     for word in words:
                            if word == '':
                                   words.pop(words.index(word))
                     print(len(words))

                     #Третий пункт
                     sentenses=re.split(r"[.?!]",fileContent) 
                     for word in sentenses:
                            if word == '':
                                   sentenses.pop(sentenses.index(word))                     
                     print(len(sentenses))

                     #Четвёртый пунктп
                     numbers=re.findall(r'\b[1-9]+\b',fileContent)                          
                     print(len(numbers))
>>>>>>> dddcb49dee654443653d5abdd37adf0962a34e50

                     #Пятый пункт
                     words_by_len = [0] * 100
                     for i in range(len(words_by_len)):
                            for word in words:
                                   if len(word) == i:
                                          words_by_len[i] += 1
                     for i in range(len(words_by_len)):
                            if (words_by_len[i] != 0):      
                                   print(f"Слов длины {i} = {words_by_len[i]}")

                     #Шестой пункт
                     max_word_len = 0
                     average_word_len = 0
                     for i in range(len(words_by_len)):
                            if words_by_len[i] != 0:
                                   average_word_len += i * words_by_len[i]
                                   if max_word_len < words_by_len[i]:
                                          max_word_len = words_by_len[i]
                     average_word_len /= len(words)
                     print(f"Максимальная длина слова = {max_word_len}")
                     print(f"Средняя длина слова = {average_word_len}")

                     #Седьмой пункт
                     




                            
       except FileNotFoundError:
              print(f"Ошибка: Файл '{dir}' не найден.")
       except Exception as e:
              print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
       main()