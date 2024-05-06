import pandas as pd
import numpy as np
def race_count(df):
    #How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
    #print("The count of people  each race are represented in this dataset",(df['race'].value_counts))
    temp=pd.Series(df['race'].value_counts())
    return (temp)

def avg_men(df):
    #What is the average age of men?
    df['sex'] = df['sex'].str.strip()  # Remove whitespace
    male_df = df[df['sex'] == 'Male'] 
    count_ofmales=male_df.shape
    sum_ofmale_age=sum(df['age'])
    #print("Average Age of male",sum_ofmale_age/count_ofmales[0])
    return (sum_ofmale_age/count_ofmales[0])

def percent_bachelors(df):
    #What is the percentage of people who have a Bachelor's degree?
    total_shapeofdataframe=df.shape
    df['education'] = df['education'].str.strip()
    bachelors_people=df[df['education']=='Bachelors'].shape
    factorial=round((bachelors_people[0]/total_shapeofdataframe[0])*100,2)
    #print("The percentage of people who have a Bachelors degree  in the data set is",factorial)
    return factorial

def percent_mast(df):
    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    total_shapeofdataframe=df.shape
    df['education'] = df['education'].str.strip()
    df['salary']=df['salary'].str.strip()
    education=df[((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df['salary']==">50K")]
    education_count=round((education.shape[0]/total_shapeofdataframe[0])*100,2)
    #print("The percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K is : ",education_count)
    return education_count

def percent_without(df):
    #What percentage of people without advanced education make more than 50K?
    total_shapeofdataframe=df.shape
    educations=df[~((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df['salary']==">50K")]
    education_counts=round((educations.shape[0]/total_shapeofdataframe[0])*100,2)
    #print("The percentage of people without advanced education make more than 50K is :", education_counts)
    return education_counts

def min_hours(df):
    #What is the minimum number of hours a person works per week?
    min_hours_per_week=(min(df['hours-per-week']))
    #print("The minimum number of hours a person works per week is:",min_hours_per_week)
    return min_hours_per_week

def percnet_minhours(df):
    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_per_week=np.min(df['hours-per-week'])
    min_hours_salary=df[(df['hours-per-week']==min_hours_per_week) & (df['salary']==">50K")]
    percentage =((min_hours_salary.shape)[0]/(df.shape)[0])*100
    #print("The percentage of the people who work the minimum number of hours per week have a salary of more than 50K is :", percentage)
    return percentage

def highest_percenatge(df):
    #What country has the highest percentage of people that earn >50K and what is that percentage?
    country_filter=df[df['salary']==">50K"]
    country_name=(country_filter['native-country'].value_counts()).idxmax()
    country_percentage=round(((np.max(country_filter['native-country'].value_counts()))/(country_filter.shape)[0])*100,2)
    #print("The Country \"{}\" has the highest percentage of people that earn >50K and the percentage is {}%".format(country_name,country_percentage))
    return (country_name,country_percentage)

def popular_occupation(df):
    #Identify the most popular occupation for those who earn >50K in India.
    df['native-country']=df['native-country'].str.strip()
    occupation_filter=df[(df['salary']==">50K" ) & (df['native-country']=='India')]
    occupation_name=(occupation_filter['occupation'].value_counts()).idxmax()
    #print("The most popular occupation for those who earn >50K in India is:",occupation_name)
    return occupation_name



