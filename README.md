# Anti-plagiarism_for_tinkoff-ML

### Description

This's an entrance project for Tinkoff-ML courses (Spring'23).

This anti-plagiarism uses the Levenshtein distance method to find a similarity score between 2 programs.

### Usage

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
   
