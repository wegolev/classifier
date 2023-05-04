from corus import load_lenta
import pandas as pd

path = 'data/lenta-ru-news.csv.gz'
records = load_lenta(path)
#print(next(records))

number_of_records = 10000
item = 1
df = pd.DataFrame(columns=['topic', 'tags', 'title'])
df_index = 0

for record in records:
    df.loc[df_index] = [record.topic, record.tags, record.title]
    df_index += 1
    if item == number_of_records:
        break

    item += 1

print(df.shape, df.dtypes, sep='\n')
print(df.head(5))