# Project Neo

## Description

This project is a hub to interface between AWS IoT and local IoT device operations. It is intended to be run on a Raspberry Pi so that messages can be passed between the two. The original motivation for this project was a stock ticker program (linked below) that I wrote a few years ago in the "Robinhood days". I thought it was a really cool project, but it had the shortcoming of being very monolithic and difficult to start/stop. I wanted to be able to schedule when this stock ticker to display, for example turning it on at market open in the mornings. I also wanted to be able to display other information, for example my local ski area's new snow for the day. 

## Installation and Usage
Long story short, the AWS side of things is complicated to get working. See this [Wiki Page](https://github.com/alyoshenka/neo/wiki/New-Teammate-Onboarding#first-steps) for an overview of some of the difficulties. Run `python[3] main.py` to start the program.

### CI - Pylint and Pytest
This project has a continuous integration system built with Pylint and Pytest. From the root project directory, run `pytest` to run tests and `./pylint.sh` to run the linter (this shell script ensures that only certain directories are linted).

## Associated Projects
- [Stock Ticker](https://github.com/alyoshenka/stockticker)

## Demo Videos

### Stock Ticker
https://user-images.githubusercontent.com/38815390/213947557-3df1d28e-a9eb-45b0-af2f-00cc65c95ecb.mp4

### Bridger Bowl Weather Report
https://user-images.githubusercontent.com/38815390/212489706-9fd0737e-c87e-478a-80a4-634295ba61ba.mp4

### AWS IoT
![light_on_off_code](https://user-images.githubusercontent.com/38815390/213949076-a0244fda-ea1f-49c8-8973-c2540d69b455.gif)

https://user-images.githubusercontent.com/38815390/213949114-48b43eee-e4c8-4fc2-a623-5c1b546663d4.mp4
