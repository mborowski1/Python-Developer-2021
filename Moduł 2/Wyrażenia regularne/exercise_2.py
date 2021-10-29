import re


with open('text.txt', 'r') as fin:
    text_to_search = fin.read()
    result_1 = re.findall(r'autor', text_to_search)
    print(result_1)
    
    result_2 = re.findall(r'[0-9]+%', text_to_search)
    print(result_2)

    result_3 = re.findall(r'\w+\.', text_to_search)
    print(result_3)

    result_4 = re.findall(r'polski', text_to_search, re.I)
    print(result_4)
