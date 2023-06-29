# Progress
- [X] Usable Chess interface  
Create a chess interface that allows users to play legal chess moves

- [X] Voice recognition from .wav to list of words (DONE)  
For voice recognition, use HuggingFace's pipeline to anaylze a .wav file recorded by the user. This outputs a list of words that will be interpreted by the chess interface

- [ ] Have Chess interface interpret output from HuggingFace pipeline to move (WIP)
  1. Create system to deal with homonyms ex. night and knight
  2. Format output from pipeline to readable chess notation
  3. Perform move based on notation inputted
