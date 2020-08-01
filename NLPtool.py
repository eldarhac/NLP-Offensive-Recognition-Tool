from googletrans import Translator
import re

# GAMATRIA = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
#             'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
#             'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60,
#             'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200,
#             'ש': 300, 'ת': 400}
MSG_PATH = 'bad_words.txt'
OUT_PATH = ''
BAD_WORDS = 'bad_words.txt'


def create_the_hash():
    words_dict = {}
    with open(BAD_WORDS) as f:
        for word in f:
            words_dict[hash(word)] = word
    return words_dict


def get_eng_trans_list(str):
    tr = Translator()
    tt = tr.translate(str)
    txt = tt.text
    return re.split("\.|\s|!|\?",txt)


def is_troll(lines):
    lst = get_eng_trans_list(lines)
    words_dict = create_the_hash()
    for word in lst:
        if words_dict.get(hash(word.lower()+"\n")):
            return True
    return False


if __name__ == '__main__':
    fileHandle = open(MSG_PATH, "r", encoding="utf-8")
    lineList = fileHandle.readlines()
    fileHandle.close()
    outFile = open(OUT_PATH, "w")
    if is_troll(" ".join(lineList)):
        print("TRUE")
        outFile.write("TRUE")
    else:
        print("FALSE")
        outFile.write("FALSE")
    outFile.close()

