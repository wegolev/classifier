import re
# import nltk
from nltk.corpus import stopwords
from corus import load_lenta
from itertools import islice

# nltk.download('stopwords')

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
# Считать первые N строк:
data_iterator = (next(records) for x in range(5))
# data = list(islice(records, 0, 100))
# оба варианта прочитают ТОЛЬКО N первых строк файла и остановятся на этом. Т.е. файл не будет читаться полностью в
# отличие от варианта с file.readlines(). Только первый вариант позволяеть сохранить исходный <class 'generator'>

data_list_lower_punctuation = []
data_list_lower_punctuation_stop_word = []
for data in data_iterator:
    data_list_lower_punctuation.append([re.sub(r'[^\w\s]', '', data.topic.lower()),
                                        (re.sub(r'[^\w\s]', '', data.title.lower())).split()])

# for data_pair in data_list_lower_punctuation:
#     for data in data_pair:
#         if print(type(data))


# print(stopwords.words('russian'))
print(len(data_list_lower_punctuation), data_list_lower_punctuation[:], sep='\n')

