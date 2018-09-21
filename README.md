# Logs-Analysis
These is a project for Udacity Full Stack Web Developer Nanodegree.

## Intorduction:
In these project we work with SQL database where we have to create a reporting tool that prints out reports in text based on the data in the database. 
The database contains a table with the information of the articles, other table with the information of the authors, and last table with log whete includes one entry for each time a user has accessed the site.
The repoting tool should answer to these questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## How to run the code:
1. Follow all the instruction of the udacity course where you have to install Vagrant and VrtualBos and where you download the file with the data.
2. To load the data use the command psql -d news -f newsdata.sql.
3. Then run pyhton catalogdb.py.
