from corus import load_lenta
from itertools import islice

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
# Считать первые N строк:
data = (next(records) for x in range(100))
# data = list(islice(records, 0, 100))
# оба варианта прочитают ТОЛЬКО N первых строк файла и остановятся на этом. Т.е. файл не будет читаться полностью в
# отличие от варианта с file.readlines(). Только первый вариант позволяеть сохранить исходный <class 'generator'>
print(type(data),  sep='\n')
# print(df.head(5))


