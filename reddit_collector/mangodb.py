#!conda install -c anaconda pymongo
from pymongo import MongoClient
import pandas as pd

df = pd.read_csv('population_data.csv')
print(df.head(2))

conn = 'localhost'
client = MongoClient(conn)
population_DB = client.population_DB
population_DB.population_table

population_DB.population_table.insert_many(df)

if __name__ == '__main__':
    for document in population_DB.population_DB_table.find():
        print(document)