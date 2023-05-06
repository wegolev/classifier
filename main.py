import re
import pandas
from nltk.corpus import stopwords
from corus import load_lenta
from nltk.stem import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

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
    data_title_stop_words = list(word for word in data_title_punctuation.split() if word not in stopwords.words('russian'))

    snowball = SnowballStemmer(language='russian')
    data_title_stem = list(map(snowball.stem, data_title_stop_words))
    

    data_clear_list.append([data_topic_punctuation, " ".join(data_title_stop_words)]) # ...stop_words преобразован из списка в строку. str() не работает. Учесть, что "".join не преобразует тип int()
print(f'len data_clear list: {len(data_clear_list)}', *data_clear_list[:5], sep='\n')

df = pandas.DataFrame(data_clear_list, columns=['topic', 'title'])
print(df)


# 1. Формирование обучающей выборки
X_train, X_test, y_train, y_test = train_test_split(df['title'], df['topic'],
                                                    train_size=0.67,
                                                    random_state=42)

print(f'len X_train: {len(X_train)}', *X_train[:5], sep='\n')
print(f'len X_test: {len(X_test)}', *X_test[:5], sep='\n')
print(f'len y_train: {len(y_train)}', *y_train[:5], sep='\n')
print(f'len y_test: {len(y_test)}', *y_test[:5], sep='\n')


# # 3. Векторизация документов: BOW
# vectorizer_bow = CountVectorizer()
# X_train_bow_vector = vectorizer_bow.fit_transform(X_train)
# print(X_train_bow_vector)