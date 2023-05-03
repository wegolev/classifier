from corus import load_lenta

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
print(next(records))

number_of_records = 1

for record in records:
    print(record.url, record.title, record.text, record.topic, record.tags, sep='\n')
    if number_of_records == 1:
        break
        