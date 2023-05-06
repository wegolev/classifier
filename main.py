import re
from nltk.corpus import stopwords
from corus import load_lenta

# from itertools import islice
# import nltk
# nltk.download('stopwords')

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
# Считать первые N строк:
data_iterator = (next(records) for x in range(5)) # Данный вариант позволяеть сохранить исходный <class 'generator'>
# data = list(islice(records, 0, 100))
# Файл не будет читаться полностью в отличие от варианта с file.readlines().

# 2. Обработка данных.:
data_clear_list = []
for data in data_iterator:
    data_topic_lower = data.topic.lower()
    data_title_lower = data.title.lower()
    data_topic_punctuation = re.sub(r'[^\w\s]', '', data_topic_lower) # Еще вариант составить список своих стоп слов
    data_title_punctuation = re.sub(r'[^\w\s]', '', data_title_lower) # и проводить сравнение с ним
    data_title_stop_word = [word for word in data_title_punctuation.split() if word not in stopwords.words('russian')]

    data_clear_list.append([data_topic_punctuation, data_title_stop_word])

print(f"len data list: {len(data_clear_list)}", *data_clear_list[:5], sep='\n') # печать списка в столбик. Еще вариант print('\n'.join(my_list))

