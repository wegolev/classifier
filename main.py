from corus import load_lenta

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
print(next(records))


