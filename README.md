# Finance-Tracker
This application is designed to make it easier for a user to track their finances. I need one and thought other people can find use for it too. :) 

# How it works

terminal -> python script -> excel spreadsheet

So to add on to the, 'work flow' above input will be provided to a python script via a terminal and the script will update an excel spreadsheet that will be on your computer locally.

# Design Questions

Input
1. Terminal
2. GUI

I decided to use terminal for getting the input over a GUI since GUI[s] in my opinion are kind of messy. 

Backend
1. Shell script
2. High level language script

I decided to use python over a shell script because I find it is easy to work with excel files in python rathen than in shell.

Output
1. Excel Spreadsheet
2. Database

I choose to store data in an Excel Spreadsheet over a Databse for a couple of reasons; they are listed below:
1. There is no installation required for Excel/CSV files compared to a database.
2. Excel or CSV files in general are supported by almost all OS[es].

I am sure not everyone will agree with the above design decision but they work for this small application and therefore I will be moving forward with them. :)
