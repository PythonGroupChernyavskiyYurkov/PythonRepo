
import argparse
import re

def main():
       parser = argparse.ArgumentParser(description='File to read')
       parser.add_argument('FileDir',type = str,help='File directory')
       arg = parser.parse_args()
       words = []
       sentenses = []
       numbers = []

       try:
              with open(arg.FileDir,'r',encoding="utf-8") as file:
                     #Чтение файла в переменную
                     file_content = file.read()

                     #Первый пункт
                     print("количество символов с пробелами: ",len(file_content))

                     fileContentNoSpaces =  file_content.replace(" ",'')
                     print("количество символов без пробелов: ",len(fileContentNoSpaces))

                     #Второй пункт
                     words=re.findall(r"\b[а-яА-Яa-zA-Z]+\b", file_content) 
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
                     for c in file_content:
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
                     words_dict = dict()
                     #Перечислены основные предлоги
                     prepositions_ru = ["без", "в", "ввиду", "во", "для", "до", "за", "из", "из-за", "ко", "на", "о", "об", "около", "от", "по", "под", "при", "про", "ради", "с", "со", "у"]
                     #Перечислены основные союзы
                     conjunctions_ru = ["и", "или", "а", "но", "же", "что", "чтобы", "как", "когда", "где", "чтобы"]
                     #Для английского соответсвенно
                     prepositions_en = ["in", "at", "on", "under", "above", "between", "to", "into", "from", "through", "along", "across", "by", "before", "after", "ago", "since", "for", "during"]
                     conjunctions_en = ["that", "as", "when", "if", "although", "and", "but", "or", "while", "where", "nor"]

                     restricted = prepositions_ru + conjunctions_ru + prepositions_en + conjunctions_en
                     for word in words:
                            word = word.lower()
                            if word in restricted:
                                   continue
                            if word in words_dict:
                                   words_dict[word] += 1
                            else:
                                   words_dict[word] = 0
                     
                     top_10 = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)[:10]
                     print("Топ 10 самых частых слов:")
                     for i in range(10):
                            print(f"{i + 1}: {top_10[i][0]}")


                     #Девятый пункт
                     bigrams = dict()
                     trigrams = dict()
                     for i in range(len(words) - 1):
                            bigram = words[i].lower() + ' ' + words[i + 1].lower()
                            if bigram in bigrams:
                                   bigrams[bigram] += 1
                            else:
                                   bigrams[bigram] = 0
                     
                     for i in range(len(words) - 2):
                            trigram = words[i].lower() + ' ' + words[i + 1].lower() + ' ' + words[i + 2]
                            if trigram in trigrams:
                                   trigrams[trigram] += 1
                            else:
                                   trigrams[trigram] = 0
                     
                     top_10_bigrams = sorted(bigrams.items(), key=lambda item: item[1], reverse=True)[:10]
                     top_10_trigrams = sorted(trigrams.items(), key=lambda item: item[1], reverse=True)[:10]
                     print()
                     print("Топ 10 самых частых биграмм:")
                     for i in range(10):
                            print(f"{i + 1}: {top_10_bigrams[i][0]}")
                     print()
                     print("Топ 10 самых частых триграмм:")
                     for i in range(10):
                            print(f"{i + 1}: {top_10_trigrams[i][0]}")


                            
       except FileNotFoundError:
              print(f"Ошибка: Файл '{dir}' не найден.")
       except Exception as e:
              print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
       main()