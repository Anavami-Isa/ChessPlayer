Word classification for Chess Player


To classify words produced by the pipeline, we are going to use the phoneme representation of words along with their lexicographical stress
	SOURCES:
		Wiki: https://en.wikipedia.org/wiki/ARPABET
		CMU phoneme dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=bee
		Research paper with similar goal: https://www.inf.ufpr.br/didonet/articles/2014_FPSS.pdf

STEPS FOR TRANSLATION:
To format speech, we will retrieve a recording(produced by the user) of the current coordinate of the piece that we want to move and the coordinate of the square that we want to move to, separated by the word "go". For example, to play the move c4 from starting position, we would say "c2 go c4".

To handle the 'voice to text' output to make a move, we will first gather the direct output of the HuggingFace model and translate each word in the output to a word that most closely matches a key in the dictionary(see words below). 

For the "c2 go c4" example, the pipeline may output something similar to "see too go sea fore". We will first break down the two coordinates(found by using the delimiter "go") in their phoneme translation. This will give an output of "[(S IY) (T UW)] go [(S IY) (F AO R)]". 

We will then search for the value of the phonemic translation in our dictionary(as seen below) and translate the output into the desired format for a command. This will give us "c 2 go c 4", which can be read by the chess program and played as a move.


Dictionary template:
FORMAT:
"Key"
	"example1" - "value1"
	"example2" - "value2"
In implementation this will look like {"Key": ["value1", "value2"]}


DICITONARY:

Go
	go - G OW1

A
	even though a is pronounced as "ah" or "eh", we are going to use the phonetic representation of "ay"(EY)
	ay - 'EY1'
	aye - 'AY1'
	eh - EH1
	a - AH0 as in hut(HH AH T)
	ale - EY1 L
	ate - EY T
B
	b - B IY1
	Bee - B IY1
C
	sea - S IY1
	see - S IY1
	c - S IY1
D
	Dee - D IY1
	Deep - D IY1 P
	Dea - D IY1
E
	E - IY
	Thee - DH 'IY'
	Cheese - CH 'IY' Z
	Green - G R 'IY' N
	Pee - P 'IY'
F
	To pronounce "F", you make an "Eff"(EH F) sound as in 'Eff'ort, not to be confused with the "F" sound in 'F'ee
	deaf - D 'EH1 F'
	Effort - 'EH1 F' ER0 T
G
	Look for "Gee"(JH IY) sound
	Jesus - 'JH IY1' Z AH0 S
	Energy - EH1 N ER0 'JH IY0'
H
	"aitch" sound
	I cannot think of a word that contains this sound. Made up words would include baitch, raitch, or daitch


1
	one - W AH1 N
2
	two - T UW1
	to - T UW1
	tooth - T UW1 TH
3
	three - TH R IY1
	tree - T R IY1
4
	four - F AO1 R
	for - F AO1 R
	fore - F AO1 R
5
	five - F AY1 V
6
	six - S IH1 K S
	sex - S EH1 K S
7
	seven - S EH1 V AH0 N
8
	eight - EY1 T
	ate - EY1 T
