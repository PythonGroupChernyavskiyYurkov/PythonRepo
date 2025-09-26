
import argparse
import re

def main():
       parser = argparse.ArgumentParser(description='File to read')

       parser.add_argument('file_dir',type = str,help='File directory')
       
       parser.add_argument('FileDir',type = str,help='File directory')
       
       arg = parser.parse_args()
       words = []
       sentenses = []
       numbers = []

       try:
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
                     alph_freq_en = [0] * 26
                     alph_cnt_en = 0
                     alph_freq_ru = [0] * 32
                     alph_cnt_ru = 0
                     for c in fileContent:
                            if c.isalpha():
                                   if c.lower() == "ё":
                                          continue
                                   if ord('a') <= ord(c.lower()) <= ord('z'):
                                          alph_freq_en[ord(c.lower()) - ord('a')] += 1
                                          alph_cnt_en += 1
                                   else:
                                          alph_freq_ru[ord(c.lower()) - ord('а')] += 1
                                          alph_cnt_ru += 1
                     for i in range(len(alph_freq_en)):
                            alph_freq_en[i] *= (100 / alph_cnt_en)
                     for i in range(len(alph_freq_ru)):
                            alph_freq_ru[i] *= (100 / alph_cnt_en)    
                     print("Частоты букв:")
                     for i in range(len(alph_freq_en)):
                            print(f"{chr(ord('a') + i)} - {alph_freq_en[i]}%")
                     for i in range(len(alph_freq_ru)):
                            print(f"{chr(ord('а') + i)} - {alph_freq_ru[i]}%")


                     #Восьмой пункт

                            
       except FileNotFoundError:
              print(f"Ошибка: Файл '{dir}' не найден.")
       except Exception as e:
              print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
       main()