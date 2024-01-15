from googletrans import Translator
import os
translater = Translator()
file = open("recognized.txt", "r+")
text = file.read()
file.truncate(0)
file.write(translater.translate(text, dest='de').text)
file.close()
