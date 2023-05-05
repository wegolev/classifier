import re
from nltk.corpus import stopwords
from corus import load_lenta
from itertools import islice

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
# Считать первые N строк:
data = (next(records) for x in range(5))
# data = list(islice(records, 0, 100))
# оба варианта прочитают ТОЛЬКО N первых строк файла и остановятся на этом. Т.е. файл не будет читаться полностью в
# отличие от варианта с file.readlines(). Только первый вариант позволяеть сохранить исходный <class 'generator'>

data_list_lower_punctuation = []
for data in data:
    # df.loc[len(df.index)] = [data.topic.lower(), data.title]
    data_list_lower_punctuation.append([re.sub(r'[^\w\s]', '', data.topic.lower()),
                                        [re.sub(r'[^\w\s]', '', data.title.lower())]])

    print(data_list_lower_punctuation[-1], sep='\n')

print(len(data_list_lower_punctuation))
