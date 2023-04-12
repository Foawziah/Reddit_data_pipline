from sqlalchemy import create_engine,text
import pandas as pd
import pymongo
import requests
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import vaderSentiment
import time
import math


logging.basicConfig(level=logging.INFO)

logging.info('Creating database connection with Mongo...')

PORT_MONGO = '27021'
CLIENT = pymongo.MongoClient('mongo_db')
DB = CLIENT.reddit_db



logging.info('Creating database connection with Postgres...')
time.sleep(15)
connection_string = 'postgresql://postgres:postgres@post_reddit:5432/reddit_data'
engine = create_engine(connection_string)
engine_connect = engine.connect()



def extract_data():
    """Read data from Mongodb"""
    cursor =DB.posts.find({})

    # Expand the cursor and construct 
    dextract_data =  list(cursor)
    print(dextract_data)
    return dextract_data

analyzer = SentimentIntensityAnalyzer()
docs= extract_data()
for doc in docs:
    print(doc)

create_table= '''
    CREATE TABLE IF NOT EXISTS reddit_table (
    text VARCHAR(500),
    sentiment NUMERIC
);
'''
engine_connect.execute(text(create_table))
engine_connect.commit()

logging.info('Extracting data from Mongo DB...')

time.sleep(2)
docs= extract_data()

logging.debug('Inserting data to PostgresDB...')
for doc in docs:
    text_ = doc['title'].replace("'", ' ').replace('\t', ' ')

    score = 1.0  # placeholder value
    query = text(f"INSERT INTO reddit_table VALUES ('{text_}', {score});")
    engine_connect.execute(query)
    engine_connect.commit()

#Save data to Postgres

