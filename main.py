import pandas as pd
import numpy as np
from demographic_data_analyzer import (
    race_count,
    avg_men,
    percent_bachelors,
    percent_mast,
    percent_without,
    min_hours,
    percnet_minhours,
    highest_percenatge,
    popular_occupation,
)

if __name__ == "__main__":
    df = pd.read_csv('adult.data', header=None)
    col = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
    df.columns = col
    # print("The count of people  each race are represented in this dataset",race_count(df))
    # print("Average Age of male",avg_men(df))
    # print("The percentage of people who have a Bachelors degree  in the data set is",percent_bachelors(df))
    # print("The percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K is : ",percent_mast(df))
    # print("The percentage of people without advanced education make more than 50K is :", percent_without(df))
    # print("The minimum number of hours a person works per week is:",min_hours(df))
    # print("The percentage of the people who work the minimum number of hours per week have a salary of more than 50K is :", percnet_minhours(df))
    # t=highest_percenatge(df)
    # print("The Country \"{}\" has the highest percentage of people that earn >50K and the percentage is {}%".format(t[0],t[1]))
    # print("The most popular occupation for those who earn >50K in India is:",popular_occupation(df))
    print(type(min_hours(df)))

    
