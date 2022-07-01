# TWEET STREAMER USING MYSQL DATABASE

## About

This project is focused on streaming live tweets that contains specified keywords into a **MYSQL** database for easy access among professionals who have been granted access to the database.

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

`database = 'specify your desired database'`

`charset = 'specify your desired encoding style' (optional)`

`host = 'specify your host'`

### Setting up the MYSQL Database

Simply launch your MYSQL Workbench, copy the contents of [tweet_db.sql]() file into a blank SQL tab and execute. This creates a database called **tweet_db**, and a table (**elections**) in the **tweet_db** database.

### Starting the Streaming App

After having setup up the neccessary files and services, simply run the below command on your terminal

`python app.py`

The terminal will then prompt you to enter the list of kweywords you want track (enter each keyword separated by a comma and hit the **enter** key on your keyboard). Voila, the streaming job should start with ease.

You can confirm that the job is running smoothly by refreshing your database at intervals to see the new tweets being streamed into the database.

#### NB:

Only seventeen (17) attributes were collected and stored into the database. If you are interested in more features, then you can tweak both the attached SQL file [tweet_db.sql]() and the python file [app.py]()

Please feel free to fork this repo if you are interested in contributing to the project as I look forward to adding addional features to the app in due time.

If you encounter any issues running the streaming job, please do not hesistate to contact me for further clarity and assitance.

## About the Author

Muhammad Abiodun Sulaiman is a graduate of Mathematics and Statistics from the prestigious Federal University of Technology, Minna, Niger State, Nigeria with Second-Class Honors. He is a smart, innovative, and seasoned analytics expert with a track record dating back to his undergraduate days.

Muhammad is a Data Science Fellow with Insight2Impact (i2i) facilities. A Microsoft Recognized Data-scientist which he bagged with an overall performance of 85%.  As a top-performing data enthusiast in the DataHack4FI Innovation Award 2019 season 3, He was awarded a gold badge (Medal). He finished up in the top 3 in the Microsoft Capstone Challenge for Mortgage Loan Approval, a Machine Learning Challenge that Involves predictive modelling. Similarly, he finished up in the top 1% in the Data Science Nigeria 2019 Artificial Intelligence preselection Kaggle Challenge, a Machine Learning Challenge that also Involves predictive modelling.

He also finished up in the top 5 Data Scientists who participated in the Data Science Nigeria 2019 AI Bootcamp pre-selection Kaggle Challenge, which involves the application of Artificial Intelligence to build an algorithmic predictive model for staff promotion.

Muhammad doubles as a Google Africa Developers Scholar and a member of the Facebook Developers Circle (DevC), he bagged in 2019, 2020 and 2021 Andela Learning Community (ALC 4.0) scholarships where he got admitted for the Google Cloud Architecture Engineering tracks consecutively.

 As a passionate self-taught Data-scientist who transitioned from being a Data Analyst, who is enthusiastic about training and helping aspiring data enthusiasts towards honing their analytical skills, He started an online coding class in collaboration with a few friends during his service year in 2019 to help interested people (graduates and nongraduates) learn how to code towards a data related career.

He is an experienced Data Scientist and Business Intelligence Analyst with a demonstrated history of working in the Research industry, extracting actionable insights from massive amounts of data, and with in-depth experience in applying advanced machine learning and data mining methods in analyzing data and in handling multiple business problems across Retail and Technology Domain. Skilled in Machine Learning, Deep Learning, Software Engineering (Backend), Statistical Modeling, Data Visualization with strong presentation and communication skills, Strong Business Development, excellent Critical Thinking and Problem-solving skills and attention to detail.

Muhammad currently works as a Data Scientist at Tsaron Technologies Limited, Lagos, Nigeria. Prior to his current role, he was a Data Scientist and Python Back-end Software Engineer at the Nigerian branch of Rhics UK. Muhammad had worked with different teams of Data Analysts/Scientists and Developers on freelance projects. He is also partnering with other innovative minds to develop solutions to varieties of problems across different sectors, health and finance inclusive.

Muhammad had over the last 5 years mentored over 20 data enthusiasts who are either into Business Analytics or Artificial Intelligence and successfully trained over 15 people on either Data Analysis, Data Science or Business Intelligence.

__Author:__ Muhammad Abiodun Sulaiman

__Email:__ abiodun.msulaiman@gmail.com

__LinkedIn:__ [Muhammad Abiodun Sulaiman](https://www.linkedin.com/in/muhammad-abiodun-sulaiman)

__Twitter:__ [@Prince_Analyst](https://www.twitter.com/Prince_Analyst)

__Facebook:__ [Muhammad Abiodun Sulaiman](https://www.facebook.com/muhammad.herbehordeun)

__Tel:__ +(234)810 831 6393

![My Pix.png](https://user-images.githubusercontent.com/45925374/140731559-e56f334c-8e89-48b8-92f7-fbe66a7447d9.png)

# THANK YOU
