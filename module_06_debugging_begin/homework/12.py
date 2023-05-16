import re

password = 'zooms'

with open('/usr/share/dict/words', 'r', encoding='utf-8') as words:
    pas_w = list()
    for file in words:
        word = file.rstrip()
        if len(word) > 4:
            pas_w.append(word)
    words = re.findall(r'\w+', password)
