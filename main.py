import pandas
import re
from corus import load_lenta
from itertools import islice

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
# Считать первые N строк:
data = (next(records) for x in range(5))
# data = list(islice(records, 0, 100))
# оба варианта прочитают ТОЛЬКО N первых строк файла и остановятся на этом. Т.е. файл не будет читаться полностью в
# отличие от варианта с file.readlines(). Только первый вариант позволяеть сохранить исходный <class 'generator'>

# df = pandas.DataFrame(columns=['topic', 'title'])
data_list = []
for data in data:
    # df.loc[len(df.index)] = [data.topic.lower(), data.title]
    data_list.append([re.sub(r'[^\w\s]', '', data.topic.lower()), re.sub(r'[^\w\s]', '', data.title.lower())])

# print(df.dtypes, df.shape, df.head(5), sep='\n'
print(len(data_list), data_list, sep='\n')
