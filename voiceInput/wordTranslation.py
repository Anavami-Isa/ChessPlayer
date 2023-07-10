import resource
import os
import re

# this class uses Carnegie Melon's Pronouncing Dictionary to translate word into their phoneme representation
class translate:
    file_name = None
    txt_file = None

    def __init__(self):
        self.file_name = "voiceInput/cmudict-07b.txt"

    def getTranslation(self, word): # takes line from dictionary and splits the word and its translation and returns the translation
        self.txt_file = open(self.file_name)
        line = self.search(word)
        translation = line.split("  ")
        self.txt_file.close()
        strippedTrans = self.strip(translation[1])
        return strippedTrans

    def strip(self, word): # removes lexiographical stress from the translation
        pattern = r'[0-9]'
        return re.sub(pattern, '', word)

    def search(self, word): # searches the dictionary for the word to be translated
        for line in self.txt_file:
            if line[0:len(word)] == word:
                return line
        return "WORD  NOTFOUND"