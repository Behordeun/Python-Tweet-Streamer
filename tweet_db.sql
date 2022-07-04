-- This sql file contains queries for creating a new database for our streaming job.
-- The script also creates a new table for storing the results of the queries.

-- Check to ensure that the database does not already exist. 
-- If it does, then delete the existing database.

-- NB: Unless you know what you are doing, please avoid using the 'DROP' function as you might not be able to restore the database (or table) after deletion.
DROP DATABASE IF EXISTS tweet_db;

-- Create a new database
CREATE DATABASE tweet_db;

-- Instruct MYSQL to use the new database.
USE tweet_db;

-- Create a new table in the new database
CREATE TABLE elections (
    created_at TIMESTAMP NOT NULL,
    tweet_id varchar(255) NOT NULL,
    tweet_text TEXT,
    cleaned_tweet TEXT,
    source VARCHAR(255),
    username VARCHAR(50),
    retweet_count INT,
    followers_count INT,
    friends_count INT,
    listed_count INT,
    favourites_count INT,
    statuses_count INT,
    following INT,
    follow_request_sent INT,
    notifications INT,
    coordinates VARCHAR(100),
    place VARCHAR(100),
    location VARCHAR(255)
)CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- Alter database to enforce character set and collation.
ALTER DATABASE 
    tweet_db 
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;