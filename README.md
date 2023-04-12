
Dockerized data pipeline that analyzes the sentiment of reddits titles.

The objective of this project is to develop a Dockerized data pipeline that can effectively analyze the sentiment of Reddit titles. The pipeline will consist of various processes orchestrated using a docker-compose.yml file. The processes will include extracting title or text data from a web-API and storing it in a MongoDB NoSQL database. The stored data will then be subjected to sentiment analysis and transformed into table format on a PostgreSQL database. Additionally, a Slack bot will be created to post selected Reddit titles in Slack.

Challenges:

There are several challenges that need to be overcome to accomplish this task, including installing Docker and ensuring all required services are running smoothly. Other challenges include collecting data from the Reddit web-API, effectively storing it in the MongoDB database, and then successfully transferring it to PostgreSQL using an ETL job. Lastly, the sentiment analysis process needs to be implemented and a Slack bot must be created.

Installation and requirements

To get started with this project, you will need to install Docker, MongoDB, PostgresDB, and vaderSentiment. Additionally, you will need to create a Reddit account and app, as well as a Slack bot. Once all requirements are met, you can build and run the project using docker-compose. To check the database on MongoDB, use the command "docker exec mongodb mongosh". Similarly, to check the table on PostgresDB, use the command "docker exec -it tahinipost psql -U postgres -h localhost -p 5432 -d reddit_db".

Install Docker Install MongoDB Install PostgresDB Install vaderSentiment
Create a Reddit account Create an app in reddit: www.reddit.com/prefs/apps Create a Slack Bot: https://api.slack.com/apps


Getting Started
docker-compose build docker-compose up docker-compose down --> removing docker container
Check database on mongodb: docker exec mongodb mongosh Check table on postgresdb: docker exec -it tahinipost psql -U postgres -h localhost -p 5432 -d reddit_db




he folder structure for this project will consist of three main components: reddit_collector, etl_job, and slackbot. The reddit_collector folder will contain files such as config.py, Dockerfile, get_reddit.py, and requirements.txt. The etl_job folder will contain config.py, Dockerfile, etl.py, and requirements.txt. The slackbot folder will contain config.py, Dockerfile, requirements.txt, and slackbot.py. Lastly, there will be a docker-compose.yml file that will bring together all the necessary components for this project to run smoothly.

The folder structure should be:
|__ reddit_collector
    |__ config.py
    |__ Dockerfile 
    |__ get_reddit.py
    |__ requirements.txt 
|__ etl_job
    |__ config.py
    |__ Dockerfile
    |__ etl.py
    |__ requirements.txt
|__slackbot
    |__ config.py
    |__ Dockerfile
    |__ requirements.txt
    |__ slackbot.py
|__ docker-compose.yml
 

# Reddit_data_pipline
