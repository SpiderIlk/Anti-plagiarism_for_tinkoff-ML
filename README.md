# Anti-plagiarism_for_tinkoff-ML

### Description

This's an entrance project for Tinkoff-ML courses (Spring'23).

This anti-plagiarism uses the Levenshtein distance method to find a similarity score between 2 programs.


### How to use


To use this anti-plagiarism you will nedd a folder with the following files:
1. ```compare.py ```
2. ```input.txt ``` 
3. ```scores.txt ```
4. some folders with programs to compare
5. folder ```files ``` with programs
6. folder ```plagiat1 ``` with programs
7. folder ```plagiat1 ``` with programs

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
   
