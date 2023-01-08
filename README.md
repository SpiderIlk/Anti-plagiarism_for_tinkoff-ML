# Anti-plagiarism_for_tinkoff-ML
This's an entrance project for Tinkoff-ML courses (Spring'23).
This anti-plagiarism uses the Levenshtein distance method to find a similarity score between 2 programs.

Пример запуска:
python3 compare.py input.txt scores.txt

Пример входного файла input.txt:

files/main.py plagiat1/main.py
files/loss.py plagiat2/loss.py
files/loss.py files/loss.py


Пример выходного файла scores.txt:
0.63
0.84
0.153
