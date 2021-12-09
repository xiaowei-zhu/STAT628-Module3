# STAT628-Module3

## Group Member

Xiaowei Zhu

Yijin Guan

Tongyue Jia

## Introduction

This project is to study the factors affecting the cocktail bars business and filtered the relevant data from Yelp. Our analysis focuses on those businesses that show 'cocktail bars' in the information of category. We mainly use the data of review text, attribute, and star to summarize some business insights and provide the owners of bars with some ways to improve the rating of their bars and attract more customers.

## Data

The raw data is too large to be uploaded and can be found at https://uwmadison.account.box.com/login?redirect_url=https%3A%2F%2Fuwmadison.app.box.com%2Fs%2F8864nymigxb3r4g2u2o5s74xspsutlrd. The data folder contains the cleaned data for our analysis.

## Image

We put all the figures we use in the slides and summary report in the image folder.

## Code

In code folder, it consists of two parts, data cleaning, preliminary analysis and model

For data cleaning, we have `data_cleaning.py` to pick out the **cocktail bars** business, `attributes.py ` to split the attributes and `review_text.py` to process the text in the review file.

For preliminary analysis, it is some initial analysis of the data, including attribute analysis and review analysis.

For model, it contains the anova analysis for attributes and review analysis based on the tf-idf values in preliminary results.

## Shiny

We put our shiny codes in the shiny folder and the link to the shiny app is: https://karina0.shinyapps.io/cocktail_bar/.
