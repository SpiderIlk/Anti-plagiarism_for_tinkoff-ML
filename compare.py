import sys
import ast


def levenshtein_distance(str_1, str_2) -> int:
    ''' finds the Levenshtein distance for 2 given strings '''
    length_1, length_2 = len(str_1), len(str_2)
    if length_1 == 0 or length_2 == 0:
        return max(length_1, length_2)
    else:
        p = [i for i in range(length_1 + 1)]  # previous row in matrix
        for i in range(1, length_2 + 1):
            d = [0] * (length_1 + 1)  # current row in matrix
            d[0] = i
            for j in range(1, length_1 + 1):
                if str_1[j - 1] == str_2[i - 1]:
                    d[j] = p[j - 1]
                else:
                    d[j] = 1 + min(d[j - 1], p[j - 1], p[j])
            p = d
        return p[-1]


def normalizer(text) -> str:
    ''' simplifies docstrings and function annotations '''
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if type(node).__name__ == 'Expr':
            node.value = ast.Constant(value='docstring')  # replace docstrings with an inscription 'docstring'
        if type(node).__name__ == 'FunctionDef':
            node.returns = None  # delete function return annotations
        if type(node).__name__ == 'arg':
            node.annotation = []  # delete function annotations
    text = ast.unparse(tree)
    return text


def compare(text1, text2) -> float:
    ''' compares 2 programs and returns a similarity score between 0 and 1 '''
    return 1 - levenshtein_distance(text1, text2) / max(len(text1), len(text2))


a = sys.argv[1:]  # read file names from command line
g = open(a[0])  # file with programs to compare
f = open(a[1], 'w')  # file 'scores' for answers
for row in g:
    r = row.split()
    f_1 = open(r[0], encoding='utf-8')  # first file to compare
    f_2 = open(r[1], encoding='utf-8')  # second file to compare
    text_1 = f_1.read()
    text_2 = f_2.read()
    text_1 = normalizer(text_1)
    text_2 = normalizer(text_2)
    f.write(str(compare(text_1, text_2)) + '\n')
    f_1.close()
    f_2.close()
f.close()
g.close()
print("it's done! Look in the 'scores' file!")
