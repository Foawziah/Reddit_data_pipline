import pandas as pd
import slack
import datetime
import asyncio
import nest_asyncio
import time
from sqlalchemy import create_engine

# connection infos
HOST_POSTGRES = 'postgres'   #Host name is the container name in docker-compose file
PORT_POSTGRES = '5432'
DBNAME_POSTGRES = 'reddit_data'
USERNAME='postgres'
PASSWORD='1234'
table='reddit_table'

while True:
    time.sleep(30)

    connection_string = 'postgres://admin:admin@postgresdb:5432/reddit_data'
    engine_postgres = create_engine(connection_string)

    #Query to select the last hour data
    query = f'''SELECT * FROM {table}
    WHERE time > (SELECT MAX(time)-INTERVAL '1 hour' FROM {table})
    ;'''

    df_recent = pd.read_sql(query, engine_postgres)

    print("Recent data loaded")
    print(df_recent.shape)

    market_sentiment = round(df_recent['sentiment'].value_counts()* 100/df_recent['sentiment'].count(),2)

    #print(f"{datetime.datetime.now()} : The crypto Market is currently {market_sentiment['neutral']}% neutral, {market_sentiment['positive']}% bullish and {market_sentiment['negative']}% bearish")
    #print('\nStrategy recommended: HODL\n')

    TEXT = f'''{datetime.datetime.now()} : The crypto Market is currently {market_sentiment['neutral']}% neutral,
    {market_sentiment['positive']}% bullish and {market_sentiment['negative']}% bearish.
    '''

    print(TEXT)


    nest_asyncio.apply()

    #Need to register an app at slack.api and get 'Bot User OAuth Access Token'
    token = '...'
    client = slack.WebClient(token=token)

    response = client.chat_postMessage(channel='#tahini-slack-bot', text=TEXT)