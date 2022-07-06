# STREAMING TWEETS INTO MYSQL DATABASE USING PYTHON

## About

This project is focused on streaming live tweets that contains specified keywords, and storing them into a specified **MYSQL** database for easy access among professionals who have been granted access to the database. The app will as well clean the tweet texts, and obtain the respective sentiment scores & labels before storing the streamed tweets into the specified database

## Running the Streaming Job

To run the streamling job, simply clone this repository by running the below command on your terminal:

`git clone https://github.com/Behordeun/tweet-streamer.git`

cd tweet-streamer

### Prerequisites

1. Twitter Developers account (with elevated access)
2. MySQL Server Installation
3. MYSQL Workbench (optional)
4. An IDE of choice (e.g., Microsoft Visual Studio Code, PyCharm, Sublime etc.)
5. Basic knowledge of SQL
6. Working knowledge of Python Programming language

Upon the creation of your Twitter Developers account, simply log into your account and create a project so you may be able to generate the needed credentials for accessing the Twitter API (Application Programming Interface) [see here for tips on getting started with Twitter Developers account](https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2).

After having successfully obtained your credentials (please keep them save and confidential as much as you can), simply create a python file (I named mine **keys.py**), and update it with the following details:

`[Twitter Developers Account Credentials]`

`access_token = "your access token" `

`access_token_secret = "your access token secret" `

`consumer_key = "your consumer key" `

`consumer_secret = "your consumer secret"`

`[MYSQL Credentials]`

`user = 'your mysql username'`

`password = 'your password'`

`database = 'specify your database name'`

`table = 'specify the table name'`

`charset = 'specify your desired encoding style' (optional)`

`host = 'specify your host'`

### Setting up the MYSQL Database

Simply launch your MYSQL Workbench, copy the contents of [tweet_db.sql](https://github.com/Behordeun/tweet-streamer-MYSQL/blob/5fc999f497bacdf01ba29659232e7a609359ce4e/tweet_db.sql) file into a blank SQL tab and execute. This creates a database called **tweet_db**, and a table (**elections**) in the **tweet_db** database.

### Starting the Streaming App

After having setup up the neccessary files and services, simply run the below command on your terminal

`python app.py`

The terminal will then prompt you to enter the list of kweywords you want track (enter each keyword separated by a comma and hit the **enter** key on your keyboard). Voila, the streaming job should start with ease.

You can confirm that the job is running smoothly by refreshing your database at intervals to see the new tweets being streamed into the database.

#### NB:

Only twenty (20) data points (attributes) were collected and stored into the database. If you are interested in more features, then you can tweak both the attached SQL file [tweet_db.sql](https://github.com/Behordeun/tweet-streamer-MYSQL/blob/5fc999f497bacdf01ba29659232e7a609359ce4e/tweet_db.sql) and the python file [app.py](https://github.com/Behordeun/tweet-streamer-MYSQL/blob/5fc999f497bacdf01ba29659232e7a609359ce4e/app.py) to suit your use case.

For safety purpose: you are not expected to commit your credentials. Hence, it is advised that you add keys.py to the **.gitignore** file.

Please feel free to fork this repo if you are interested in contributing to the project as I look forward to adding addional features to the app in due time.

If you encounter any issues running the streaming job, please do not hesistate to contact me for further clarity and assitance.

## About the Author

Muhammad Abiodun Sulaiman is a data analytics professional with vast experience spread across **Data Science and Business Intelligence.** He is a Cloud DevOps Engineering enthusiat who is skilled at **Infrastructure as Code** using tools such as **Terraform, Docker, Kubernetes, Ansible, AWS Cloudformation, AWS Cloudwatch, etc.,**

He currently works at **Tsaron Technologies Limited** as a **Telematics Data Scientist**, and is specialized at building **Machine Learning models** for **Scoring** and **Classifying** drivers into different **safety zones** based on their **driving behaviours**.

He can be contacted via the following medium:

1. __Email:__ abiodun.msulaiman@gmail.com
2. __LinkedIn:__[Muhammad Abiodun Sulaiman](https://www.linkedin.com/in/muhammad-abiodun-sulaiman)
3. __Twitter:__[@Prince_Analyst](https://www.twitter.com/Prince_Analyst)
4. __Facebook:__[Muhammad Abiodun Sulaiman](https://www.facebook.com/muhammad.herbehordeun)
5. __Tel:__ +(234)810 831 6393

***THANK YOU FOR TRYING OUT MY APP***
