# Anti-plagiarism_for_tinkoff-ML

### Description

This's an entrance project for Tinkoff-ML courses (Spring'23).

This anti-plagiarism uses the Levenshtein distance method to find a similarity score between 2 programs.


### How to use


To use this anti-plagiarism you will need a folder on your computer with the following files:
1. ```compare.py```
2. input.txt
3. scores.txt
4. some folders with programs to compare

input.txt is a file with pairs of paths to compared files.   scores.txt is a file in which similarity scores will be written.   In an example below I'll use folders: files, plagiat1 and plagiat2.   You can find them in this repository.   The anti-plagiarism can be launched using the Command line.

Launch example:
   ```sh
   python3 compare.py input.txt scores.txt
   ```
Example of input file input.txt:
   ```sh
    files/main.py plagiat1/main.py
    files/lossy.py plagiat2/lossy.py
    files/lossy.py files/lossy.py
   ```
Example of output file scores.txt:
   ```sh
   0.63
   0.84
   0.153
   ```
   
