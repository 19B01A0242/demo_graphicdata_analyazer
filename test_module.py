import pandas as pd
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

# Load the dataset
df = pd.read_csv('adult.data', header=None)
col = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
df.columns = col

#Test race_count function
def test_race_count():
    result = race_count(df)
    assert isinstance(result, pd.Series), "race_count should return a Pandas Series"
    #assert result.sum() == df.shape[0], "Sum of race counts should equal the total number of rows in the dataset"
    #assert isinstance(result, pd.Series)
    print("race_count function passed successfully!")

# Test avg_men function
def test_avg_men():
    result = avg_men(df)
    assert isinstance(result, float), "avg_men should return a floating-point number"
    print("avg_men function passed successfully!")

# Test percent_bachelors function
def test_percent_bachelors():
    result = percent_bachelors(df)
    assert isinstance(result, float), "percent_bachelors should return a floating-point number"
    print("percent_bachelors function passed successfully!")

# Test percent_mast function
def test_percent_mast():
    result = percent_mast(df)
    assert isinstance(result, float), "percent_mast should return a floating-point number"
    print("percent_mast function passed successfully!")

# Test percent_without function
def test_percent_without():
    result = percent_without(df)
    assert isinstance(result, float), "percent_without should return a floating-point number"
    print("percent_without function passed successfully!")

# Test min_hours function
def test_min_hours():
    result = min_hours(df)
    assert isinstance(result, int), "min_hours should return an integer"
    print("min_hours function passed successfully!")

# Test percnet_minhours function
def test_percnet_minhours():
    result = percnet_minhours(df)
    assert isinstance(result, float), "percnet_minhours should return a floating-point number"
    print("percnet_minhours function passed successfully!")

# Test highest_percenatge function
def test_highest_percenatge():
    result = highest_percenatge(df)
    assert isinstance(result, tuple), "highest_percenatge should return a tuple"
    assert len(result) == 2, "highest_percenatge should return a tuple of length 2"
    print("highest_percenatge function passed successfully!")

# Test popular_occupation function
def test_popular_occupation():
    result = popular_occupation(df)
    assert isinstance(result, str), "popular_occupation should return a string"
    print("popular_occupation function passed successfully!")

# Run all the test functions
if __name__ == "__main__":
    test_race_count()
    test_avg_men()
    test_percent_bachelors()
    test_percent_mast()
    test_percent_without()
    test_min_hours()
    test_percnet_minhours()
    test_highest_percenatge()
    test_popular_occupation()
