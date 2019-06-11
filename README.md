# Explore US Bikeshare Data
This Python script was written for a project in Udacity's Data Analyst Nanodegree (DAND) and is used to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from csv files and computes descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

## Running the Script
You can run the script using a Python integrated development environment (IDE). Additionally, this script was written in Python 3. As such, you'll need the Python 3.x version in your IDE.

## The Datasets
The datasets used for this script contain bike share data for the first six months of 2017, provided by Motivate (a US bike share system provider). The datasets are from the cities New York City, Chicago, and Washington DC. Some data wrangling had been performed by Udacity's staff before being provided to the students of DAND. Due to the large file sizes of the datasets (~35 mbs each), they were not uploaded to this GitHub repository. Instead, I have uploaded them to [this](https://drive.google.com/drive/folders/1RhekKGML9dg4J4vEDBHJJm7ddNEXtDNF?usp=sharing) Google Drive folder instead. In order to run the script, download and place the files (unzipped) in the same folder as the Python script.

The data files for all three cities contain the same six columns:
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
* Gender
* Birth Year

## Questions Explored
The script answers the following questions about the bike share data:

#### Time Stats
* What is the most common month for start time?
* What is the most common day of week for start time?
* What is the most common start hour of the day?

#### Station Stats
* What is the most popular start station?
* What is the most popular end station?
* What is the most popular start and end station trip?

#### Trip Duration Stats
* What is the total trip duration?
* What is the average trip duration?

#### User Stats
* What are the counts for each user type?
* What are the counts for gender?
* What are the earliest (oldest age), most recent (youngest age), and most popular birth years?

