from transformers import pipeline
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from wordTranslation import translate


class SpeechRecognition:
    freq = None
    seconds = None
    recording = None
    translator = None
    colTrans = {"AH": "a", "B IY": "b", "S IY": "c", "D IY": "d", "IY": "e", "EH F": "f", "JH IY": "g", "EY CH": "h"}
    rowTrans = {"EY T": 8, "S EH V AH N": 7, "S IH K S": 6, "F AY V": 5, "F AO R": 4, "TH R IY": 3, "T UW": 2, "W AH N": 1}

    def __init__(self):
        self.freq = 44100
        self.seconds = 5
        self.translator = translate()

    def run(self):
        self.getCommand()
    
    def getCommand(self):
        self.record()
        command = self.splitCoords(self.recordingToWords())
        return command 

    def record(self): # Takes audio input and stores it in .wav file
        print("Recording")
        self.recording = sd.rec(int(self.seconds * self.freq),
                        samplerate=self.freq, channels=1)
        sd.wait()

        print("Finished Recording")
        write("output0.wav", self.freq, self.recording)

    def recordingToWords(self): # Takes .wav file and words in audio file as array
        # Convert the NumPy array to audio file
        wv.write("output1.wav", self.recording, self.freq, sampwidth=2)

        cls = pipeline("automatic-speech-recognition")
        res = cls("output1.wav")
        listOfWords = res["text"].split(" ")
        print("Raw interpretation: " + str(listOfWords))
        return listOfWords
    
    def splitCoords(self, listOfWords): # Takes array of words, checks format, and returns the translation of the coordinates
        delimiter = False
        middle = 0
        for word in listOfWords:
            if self.translator.getTranslation(word.upper()).strip() == "G OW":
                delimiter = True
                break
            middle += 1
        if not delimiter:
            print("Error: Delimiter \"Go\" not found")
            return
        if middle != 2:
            print("Error: first argument not of length 2")
            return
        if len(listOfWords) != 5:
            print("Error: second argument not of length 2")
            return
        startPos = self.fixCoordinate(listOfWords[0:2])
        endPos = self.fixCoordinate(listOfWords[3:5])
        start = startPos[0] + str(startPos[1])
        end = endPos[0] + str(endPos[1])
        return (start + " -- " + end)
        
        
    def fixCoordinate(self, coordinate): # uses translator to return legible command for chess engine
        pCol = self.translator.getTranslation(coordinate[0]).strip()
        pRow = self.translator.getTranslation(coordinate[1]).strip()
        col = self.colTrans[pCol]
        row = self.rowTrans[pRow]
        return (col, row)